box = None
temp = None
for i in range( 20,41 ) :
 if i % 3 == 0 :
  temp = ListNode( i )
  temp.next = box
  box = temp
