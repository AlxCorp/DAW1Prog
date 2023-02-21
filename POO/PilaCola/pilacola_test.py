from pilacola import Stack, Queue

s1 = Stack()
s2 = Stack(s1)

s1.storage = "Hola"
s1.storage = 2135234
s1.storage = 41.42
s1.storage = input("ALGO: ")
print(s1.storage)

print(s1.size)
print(s1.is_used)
print(s1.empty())
print(s1.size)

print(s1.push("holacaracola"))
print(s1.pop())
print(s1.top)
print(s1.push("1"))
print(s1.push("2"))
print(s1.push("3"))
print(s1.push(4))
print(s1.top)


# -------------------------------------------------------- #

q1 = Queue()
q2 = Queue(q1)

q1.storage = "Hola"
q1.storage = 2135234
q1.storage = 41.42
q1.storage = input("ALGO: ")
print(q1.storage)

print(q1.size)
print(q1.is_used)
print(q1.empty())
print(q1.size)

print(q1.enqueue("holacaracola"))
print(q1.dequeue())
print(q1.front)
print(q1.enqueue("1"))
print(q1.enqueue("2"))
print(q1.enqueue("3"))
print(q1.enqueue(4))
print(q1.front)
