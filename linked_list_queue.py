class ListNode():
  def __init__ (self, val=0, next=None):
    self.val = val
    self.next = next

  def __str__(self):
    res = '[' + str(self.val) + ', '
    if self.next:
      res += str(self.next)
    else:
      res += "None"
    return res + ']'

class Queue():
  def __init__(self, val=None):
    self.head = ListNode(val)
    self.tail = self.head
    self.cnode = self.head

  def __str__(self):
    return str(self.head)

  def is_empty(self):
    return True if self.head.val == None else False

  def peek(self):
    return False if self.is_empty() else self.head.val

  def pop(self):
    res = self.head.val
    if self.head.next == None:
      self.head.val = None
    else:
      self.head = self.head.next
    return res

  def push(self, val=0):
    if self.head.val == None:
      self.head.val = val
      return
    self.cnode = ListNode(val)
    self.cnode.next = self.head
    self.head = self.cnode

  def append(self, val=0):
    new_node = ListNode(val)
    self.tail.next = new_node
    self.tail = self.tail.next

  def insert(self, val=0, n=0):
    if not n:
      self.push(val)
      return

    new_node = ListNode(val)
    self.cnode = self.head

    while n > 1 and self.cnode.next:
      self.cnode = self.cnode.next
      n -= 1

    new_node.next = self.cnode.next
    self.cnode.next = new_node

  def reverse(self):
    if not self.cnode.next:
      return

    self.tail = self.head
    self.cnode = self.head.next
    pnode = self.head
    pnode.next = None

    while self.cnode:
      nnode = self.cnode.next
      self.cnode.next = pnode
      pnode = self.cnode
      self.cnode = nnode

    self.head = pnode

if __name__ == "__main__":
  queue = Queue()
  queue.push(1)
  queue.push(5)
  queue.pop()
  queue.insert(3, 1)
  queue.insert(4, 1)
  queue.insert(6, 2)
  print('contents:', queue)
  queue.reverse()
  queue.append(10)
  print('peek val:', queue.peek())
  print('contents:', queue)
  while not queue.is_empty():
    print(queue.pop())
  print('empty status:', queue.is_empty())
  print('queue contents:', queue)