
#program to check brackets in order
#question asked in IDFC
a=[]
b=True
c="{[[]]}"
for x in c:
  if x in '{[(':
    a.append(x)
  elif x in '}])':
    if not(a):
      b=False
      break
    else:
      match x:
        case '}':
          if a.pop()!='{':
            b=False
        case ']':
          if a.pop()!='[':
            b=False
        case ')':
          if a.pop()!='(':
            b=False
print(b)

#2 counting pairs
a=[1,2,3,4,5,6,7]
target=4
seen=set()
for x in a:
  temp=target-x
  if temp in seen:
    print("{}{}".format(temp,x))
  seen.add(x)

#mapping status
class Report:
  def __init__(self,status):
    self.attempt=1
    self.firststatus=status
    self.laststatus=status
    self.flaky=False
data={}
results = [
  ["checkout_test", "attempt-1", "FAIL"],
  ["checkout_test", "attempt-2", "PASS"],
  ["login_test", "attempt-1", "PASS"],
  ["search_test", "attempt-1", "FAIL"],
  ["search_test", "attempt-2", "FAIL"],
  ["profile_test", "attempt-1", "PASS"],
  ["profile_test", "attempt-2", "FAIL"],
  ["cart_test", "attempt-1", "SKIP"]
]
for temp in results:
  testname=temp[0]
  status=temp[2]
  if testname not in data:
    data[testname]=Report(status)
  else:
    rt=data[testname]
    rt.attempt+=1
    rt.finalstatus=status
    if rt.firststatus!=rt.finalstatus:
      rt.flaky=True
print(f"{'Testname':<15}{'Attempt':<15}{'Status':<15}{'Flaky':<15}")
print('_'*60)

for testname,Report in data.items():
  print(f"{testname:<15}" f"{Report.attempt:<15}" f"{Report.laststatus:<15}" f"{Report.flaky:<15}")



