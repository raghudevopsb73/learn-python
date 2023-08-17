import threading
import subprocess


def instance_create(node):
    tagName = "'ResourceType=instance,Tags=[{Key=Name,Value=" + node + "}]'"
    print(tagName)
    out = subprocess.run(
        ["aws", "ec2", "run-instances", "--image-id", "ami-03265a0778a880afb", "--instance-type", "t3.micro", "--tag-specifications", tagName ],
        capture_output=True, text=True)
    print(out.stderr)


nodes = ["node1", "node2", "node3"]
threadCount = []

for node in nodes:
    thread = threading.Thread(target=instance_create(node))
    threadCount.append(thread)
    thread.start()

for thread in threadCount:
    thread.join()
