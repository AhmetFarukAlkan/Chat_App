from vidstream import AudioSender
from vidstream import AudioReceiver
import threading
import  socket

receiver = AudioReceiver('10.123.12.206', 4000)
#receiver = AudioReceiver('25.73.110.228', 8888)#me sesi gönderen

sender = AudioSender('10.123.12.75', 4000)#he/she sesi alan
#sender = AudioSender('25.73.147.77', 8888)#he/she sesi alan

sender_thread = threading.Thread(target=sender.start_stream)
receive_thread = threading.Thread(target=receiver.start_server)

receive_thread.start()
sender_thread.start()