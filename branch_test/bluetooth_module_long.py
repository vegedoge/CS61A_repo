'''
File name: bluetooth_module_long.py
Author: WU Yuxuan
Created time: 2024.1.12
Description: Enable pi to communicate by bluetooth, mainly test
its pairing, connection and json file transmission function.
'''

import bluetooth
import json
import subprocess
import socket
import time
import threading
import pdb
import queue
import os

class BluetoothModule:
    '''
    block 0, dont set event, 1 set event
    event set for refresh
    '''
    def __init__(self, event, block = 0):
        
        self.block = block
        self.event = event
        # pdb.set_trace()
        print("BT start")
        self.data_to_send = queue.Queue()
        # self.data_to_send.put("0000")
        
        # state for bt connection
        # 0 for disconnected, 1 for connected
        self.state = 0
        
        
    # def start_bluetooth_thread(self):
        # self.bluetooth_thread = threading.Thread(target=self.run_server, args=(self.data_to_send,))
        self.bluetooth_thread = threading.Thread(target=self.run_server)
        self.bluetooth_thread.setDaemon(True)
        self.bluetooth_thread.start()
        
        # thread_capture = threading.Thread(target=self.update_status, args=(self.initial_status,))
        # thread_capture.setDaemon(True)
        # thread_capture.start()
        
    def update_data(self, data_to_send):
        '''update data_to_send'''
        print(f'updated {data_to_send}')
        if self.data_to_send.empty():
            self.data_to_send.put(data_to_send)
        else:
            # dump jammed data while disconnected with cell phone
            print(f'data jammed')
            jammed_data = self.data_to_send.get()
            self.data_to_send.put(data_to_send)
            


    def enable_discoverable(self):
        '''
        Control shell out of py, enable BT discoverability
        '''
        subprocess.run(["sudo", "hciconfig", "hci0", "piscan"]) 
        
    def send_to_device(self, data_to_send, client_socket):
        '''
        Send json message to connected BT device
        '''   
        # turn json into string
        json_string = json.dumps(data_to_send.get())

        # json send
        client_socket.send(json_string.encode())
        time.sleep(1)
        
    def send_binary_file(self, file_path, client_socket, chunk_size = 512):
        '''send image binary file
        1. send chunk size, the numbers of packages to be sent
        2. send image file packages 
        '''
        try:
            file_size = os.path.getsize(file_path)
            # calculate total division number
            total_chunks = (file_size + chunk_size - 1) // chunk_size
            client_socket.send(str(total_chunks).encode())
            time.sleep(1)
                
            with open(file_path, 'rb') as file:
                # read from file 
                data = file.read(chunk_size)
                while data:     
                    client_socket.send(data)
                    data = file.read(chunk_size)

            print("Binary file sent successfully")

        except Exception as e:
            print(f"Error while sending files: {str(e)}")
        
    def receiving_from_device(self, client_socket):
        '''
        Start receiving data from cell phone,
        only catch once, ONCE received, return
        '''
        # try receiving from cell phone
        try:
            client_socket.settimeout(1)
            
            # max receivec 1024 bytes
            data = client_socket.recv(1024)
            if not data:
                print("Connection closed by the device.")
                return None
            return data
        
        except bluetooth.btcommon.BluetoothError as e:
            if "timed out" in str(e):
                print("Receive timeout! No data received.")
            elif "Resource temporarily unavailable" in str(e):
                print("Connection temporarily unavailable. Reconnecting...")
                self.state = 0
            else:
                print(f"Receive error: {str(e)}")
            return None
            
        except KeyboardInterrupt:
            print("Interrupted")
            return None


    def run_server(self):
        
        try:
            self.enable_discoverable()
            self.server_socket = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
            
            # channel port is free to choose
            self.server_socket.bind(("", bluetooth.PORT_ANY))
            self.server_socket.listen(1)
            port = self.server_socket.getsockname()[1]
            print(f"waiting for cell phone connection from channel {port}")
            # Set timeout to 1 seconds
            self.server_socket.settimeout(1)

            while True:
                try:
                    # disconnected state, keep retrying
                    if self.state == 0:
                        self.client_socket, address = self.server_socket.accept()
                        print("cell phone connection from ", address)
                        self.state = 1
                    # connected state, run missions   
                    elif self.state == 1:
                        # receive data from client, if needed
                        received_data = self.receiving_from_device(self.client_socket)
                        if not received_data:
                            print("No data received")
                        else:
                            # received data decode and print
                            received_data = received_data.decode('utf-8', errors = 'ignore')
                            print("received message: ", received_data)
                            # if blocked, won't set event
                            if self.block == 0:
                                self.event.set()
                            
                            # start image transmission
                            # self.image_file_path = "/home/pi/ffd_demo/tiny_test.jpg"
                            
                            # self.image_file_path = self.latest_pic()
                            # self.send_binary_file(self.image_file_path, self.client_socket)
                            # print("image sent successfully")
                        
                        if not self.data_to_send.empty(): 
                            # send json data to client
                            self.send_to_device(self.data_to_send, self.client_socket)
                            print("json sent successfully")
                            
                            # start image transmission
                            # self.image_file_path = "/home/pi/ffd_demo/tiny_test.jpg"
                            self.image_file_path = self.latest_pic()
                            self.send_binary_file(self.image_file_path, self.client_socket)
                            print("image sent successfully")
                        else:
                            print("BTlong.py : no updated data now")
                except bluetooth.btcommon.BluetoothError as e:
                    if "timed out" in str(e):
                        print("Connecting timeout! No cell phone connected.")
                    else:
                        print(f"Connection error: {str(e)}")

                    # client close
                    # client_socket.close()
                    
        
        except bluetooth.btcommon.BluetoothError as e:
            if "timed out" in str(e):
                print("Connecting timeout! No cell phone connected.")
            else:
                print(f"Connection error: {str(e)}")
            
        except KeyboardInterrupt:
            print("Interrupted")

        finally:
            # Connection finished
            # server_socket.close()  
            print("bt transmission finished")
      
            
    def latest_pic(self):
        # select picture by time
        picture_folder_path = "/home/pi/ffd_demo/ffd_picture"
        # pictures = [f for f in os.listdir(picture_folder_path) 
        #                 if os.path.isdir(os.path.join(picture_folder_path, f))]
        
        pictures = [f for f in os.listdir(picture_folder_path) 
                    if f.lower().endswith(('.png', '.jpg', '.jpeg'))]

        # choose latest subfolder path
        # sort by time
        pictures.sort(key=lambda f: os.path.getmtime(os.path.join(picture_folder_path, f)))
        latest_picture = pictures[-1]
        latest_picture_path = os.path.join(picture_folder_path, latest_picture)
        # path reload
        image_path = latest_picture_path
        return image_path
    
    

if __name__ == "__main__":
    # json data to be sent --test
    data_to_send1 = {
        "column": 1, "blueberry_exist": 0, "beef_exist": 0, "cv_worst_blueberry": 0, "cv_worst_beef": 0, "EN Freshness": 1}, {"column": 2, "blueberry_exist": 0, "beef_exist": 1, "cv_worst_blueberry": -1, "cv_worst_beef": 2, "EN Freshness": 1}, {"column": 3, "blueberry_exist": 0, "beef_exist": 0, "cv_worst_blueberry": -1, "cv_worst_beef": -1, "EN Freshness": 1}, {"column": 4, "blueberry_exist": 0, "beef_exist": 0, "cv_worst_blueberry": -1, "cv_worst_beef": -1, "EN Freshness": 1
    }
    data_to_send2 = {
        "column": 1, "blueberry_exist": 1, "beef_exist": 1, "cv_worst_blueberry": 1, "cv_worst_beef": 1, "EN Freshness": 1}, {"column": 2, "blueberry_exist": 0, "beef_exist": 1, "cv_worst_blueberry": -1, "cv_worst_beef": 2, "EN Freshness": 1}, {"column": 3, "blueberry_exist": 0, "beef_exist": 0, "cv_worst_blueberry": -1, "cv_worst_beef": -1, "EN Freshness": 1}, {"column": 4, "blueberry_exist": 0, "beef_exist": 0, "cv_worst_blueberry": -1, "cv_worst_beef": -1, "EN Freshness": 1
    }
        
    data_to_send = data_to_send1   
    refresh_event = threading.Event()
    flag = 0
    
    BT = BluetoothModule(refresh_event)
    # BT.start_bluetooth_thread()
    # BT.bluetooth_thread.join()
    BT.update_data(data_to_send)
    
    while True:
        print("main still running")
        flag = flag + 1
        time.sleep(10)
        # shift test
        if refresh_event.is_set():
            print("event triggered")
            refresh_event.clear()
            
        if flag % 2 == 0:
            data_to_send = data_to_send1
        else:
            data_to_send = data_to_send2
        BT.update_data(data_to_send)
