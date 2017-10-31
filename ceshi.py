list1=[1,2,3,4,5,6,7]
list2=['a','b','c','d']
list3=[]
i=0
for i in range(len(list2)):
    list3.append({'id':list1[i],'password':list2[i]})
    i+=1
print(list3)
# import ddt,unittest
# data=[{1:1, 2:2},{1:2, 2:3},{1:3, 2:4}]
# @ddt.ddt
# class Testcase(unittest.TestCase):
#     def setUp(self):
#         pass
#     def tearDown(self):
#         pass
#     @ddt.data(*data)
#     def test(self,data):
#         self.assertEqual(data[1],data[2])
# if __name__=='__main__':
#     unittest.main()
