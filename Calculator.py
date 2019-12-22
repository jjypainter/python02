class Calculator:

    def _init_(self,data):
        self.data=data

     def sum(self):
         self.sum=0
          for i in self.data:
              self.sum+=i
          print(self.sum)

     def avg(self):
         self.avg=self.sum/len(self.data)
         print(self.avg)

cal1=Calculator([1,2,3,4,5])
cal1.sum()
cal1.avg()
cal2=Calculator([6,7,8,9,10])
cal2.sum()
cal2.avg()

