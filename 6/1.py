with open('input') as f:
    text = f.read()

queue = []
for i, c in enumerate(text):
    if len(queue) > 3:
        queue.pop(0)
    queue.append(c)
    if len(set(queue)) == 4:
        print(i+1)
        print(queue)
        break
