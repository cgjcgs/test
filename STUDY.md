line_profiler工具分析代码性能

pip install line_profiler
在需分析的方法上面加上 @profile 
kernprof -l -v sync_block.py 

	Line #      Hits         Time  Per Hit   % Time  Line Contents
	==============================================================
	    6                                           @profile
	    7                                           def blocking_way():
	    8        10        355.0     35.5      0.0  	sock = socket.socket()
	    9                                           	#blocking
	    10        10    1933242.0 193324.2     33.3  	sock.connect(('example.com',80))
	    11        10         97.0      9.7      0.0  	request = 'GET / HTTP/1.0\r\nHost: example.com\r\n\r\n'
	    12        10       1023.0    102.3      0.0  	sock.send(request.encode('ascii'))
	    13        10        106.0     10.6      0.0  	response = b''
	    14        10    3870093.0 387009.3     66.7  	chunk = sock.recv(4096)
	    15        20        118.0      5.9      0.0  	while chunk:
	    16        10         29.0      2.9      0.0  		response += chunk
	    17        10        162.0     16.2      0.0  		chunk = sock.recv(4096)
	    18        10         14.0      1.4      0.0  	return response

