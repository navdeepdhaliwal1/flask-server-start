from flask import Flask
import psutil

app = Flask(__name__)

@app.route('/')
def stats():
    cpu = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory()
    disk = psutil.disk_usage('/')

    return f"""
    <html>
    <head><title>Server Stats</title></head>
    <body style="font-family:sans-serif; padding:40px;">
        <h1>Server Health Dashboard</h1>
        <h3>CPU Usage: {cpu}%</h3>
        <h3>Memory: {memory.percent}% used
            ({round(memory.used/1024**3, 1)}GB
            / {round(memory.total/1024**3, 1)}GB)</h3>
        <h3>Disk: {disk.percent}% used
            ({round(disk.used/1024**3, 1)}GB
            / {round(disk.total/1024**3, 1)}GB)</h3>
    </body>
    </html>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
