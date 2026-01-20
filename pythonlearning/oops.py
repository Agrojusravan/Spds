#!/usr/bin/env python
# coding: utf-8

# # creating a class

# In[15]:


class Student_info:
    '''this class is going to info a students'''
    def __init__(self,name,rollno,course):
        self.name=name
        self.rollno=rollno
        self.course=course
    def info(self):
        '''this give me the record of students'''
        return f"({self.name} whose rollno is {self.rollno} has been enrolled in the course named {self.course})" 


# # creating an object 

# In[16]:


stu1 = Student_info("sravan",9,"DA")


# In[17]:


stu1.info


# In[18]:


stu1.info()


# In[16]:


stu1.course


# In[17]:


stu1.name


# In[18]:


stu1.rollno


# # creating another class

# In[34]:


class Student_info:
    '''this class is going to info a students'''
    def __init__(ram,name,rollno,course):
        ram.name=name
        ram.rollno=rollno
        ram.course=course
    def info(ram):
        '''this give me the record of students'''
        return f"({ram.name} whose rollno is {ram.rollno} has been enrolled in the course named {ram.course})" 


# In[35]:


stu1 = Student_info("sravan",9,"DA")


# In[36]:


stu1.course


# In[56]:


stu1.info()


# # creating a class without a counstructor

# In[19]:


class Student_info_without_constructor:

    def info(self,name,roll,course):
        self.name=name
        self.roll=roll
        self.course=course
        return f"({self.name} whose roll is {self.roll} has benn enrolled in the cource named {self.course})"


# In[20]:


stu4 = Student_info_without_constructor()


# In[21]:


stu4.info("sai",9,"DA")


# In[22]:


stu4.course


# In[23]:


stu4.name


# # types of variables

# ## class variables also know as static variable

# # 1 inside a class outside a consturctor and methos

# In[32]:


class Student:
    college = "ABC" #static variable

    def __init__(self,name):
        self.name = name
    def info(self):
        return f"(the name of student {self.name} whose belong to college {self.college})"


# In[33]:


st = Student("sravan")


# In[34]:


st.college


# In[35]:


st.info()


# # 2 inside the constuctor outside function

# In[43]:


class Student:
     def __init__(self,name):
         Student.school="ims" # static variable
         self.name = name
     def info(self):
         return f"(the name of student {self.name} whose belong to college {self.school})"
        


# In[59]:


st6 = Student("avan")


# In[60]:


st6.info()


# # 3 imside the method

# In[71]:


class Student1:
    def __init__(self,name):
        self.name=name
    def info(self):
        Student1.sschool="imms"
        return f"(the name of student {self.name} whose belong to college {self.sschool})"


# In[74]:


st7 = Student1("avan")


# In[75]:


st7.info()


# # outside the class

# In[82]:


class Student:
    def __init__(self,name):
        self.name=name
    def info(self):
        return f"(the name of student {self.name} whose belong to sschool {self.sschool})"


# In[83]:


st8 = Student("ram")


# In[84]:


st8.info()


# In[85]:


Student.sschool="immmss"


# In[86]:


st8.sschool


# In[87]:


st8.info()


# # instance variable

# ## inside a constructor

# In[92]:


class Student:
    def __init__(self,name):
        self.name=name
    def info(self):
        return f"(the name is {self.name})"


# In[93]:


st9 = Student("srvan")


# In[94]:


st9.info()


# ## inside a methdo

# In[115]:


class Student:
    def __init__(self,name):
        self.name=name
    def info(self):
        self.age=22
        return f"(the name is {self.name} and age is {self.age})"


# In[116]:


st10= Student("sravan")


# In[117]:


st10.info()


# ## out side class

# In[5]:


class Student:
    def __init__(self,name):
        self.name=name
    def info(self):
        return f"(the name of student {self.name} and age is {self.age})"


# In[6]:


st11 = Student("name")


# In[7]:


Student.age=22


# In[8]:


st11.info()


# In[9]:


st11.age


# # local variable

# In[15]:


class Studen:

     def info(self,name,roll,course):
        self.name=name
        self.roll=roll
        self.course=course
        return f"({self.name} whose roll is {self.roll} has benn enrolled in the cource named {self.course})"


# In[18]:


st88 = Studen()


# In[19]:


st88.info("sravan",23,"ds")


# In[20]:


st88.course


# # define static variable again and again

# In[21]:


class school:
    course = "ABC"
    def __init__(self):
        school="XYZ"
    def info(self):
        school="pqr"
        return f"the school name is should ne pqr as i have a static variable defined inside a mthod"
        


# In[23]:


school.course="mno"


# In[25]:


school.course


# In[26]:


obj = school()


# In[27]:


obj.course


# # features of oops
#  * inheritance
#  * encapusulation
#  * polymorphism
#  * abstraction
# 

# # Inheritance

# ## single inheritance

# In[60]:


class Parent:
    def __init__(self,pname):
        self.pname=pname
        
    def info_p(self):
        return f"this method belog to parent"


# In[61]:


class Child(Parent):
    def __init__(self,cname,pname):
        super().__init__(pname)
        self.cname=cname
        
    def info_c(self):
        return f"this method belog to child"


# In[62]:


c = Child("c","p")


# In[63]:


c.pname


# In[64]:


c.info_c()


# In[65]:


c.cname


# In[66]:


c.info_p()


# ## multi level inheritance

# In[67]:


class Grandparent:
    def __init__(self,gname):
        self.gname=gname
    def info_g(self):
        return f"this method belogs to grand parent"   
class Parent(Grandparent):
    def __init__(self,pname,gname):
        super().__init__(gname)
        self.pname=pname
        
    def info_p(self):
        return f"this method belog to parent"
class Child(Parent):
    def __init__(self,cname,pname,gname):
        super().__init__(pname,gname)
        self.cname=cname
        
    def info_c(self):
        return f"this method belog to child"


# In[68]:


c = Child("s","r","a")


# In[69]:


c.gname


# In[70]:


c.cname


# In[71]:


c.pname


# In[73]:


c.info_c()


# In[74]:


c.info_p()


# In[75]:


c.info_g()


# ## multipule inheritance

# In[103]:


class Father:
    def __init__(self,fname):
        self.fname=fname
    def info_f(self):
        return f"this a father class"
class Mother:
    def __init__(self,mname):
        self.mname=mname
    def info_m(self):
        return f"this is mother class"
class Child(Father,Mother):
    def __init__(self,cname,fname,mname):
        self.cname=cname
        Father.__init__(self,fname)
        Mother.__init__(self,mname)
    def info_c(self,age):
        self.age=5
        return f"this is child class {self.age}"


# In[104]:


c3=Child("a","v","k")


# In[105]:


c3.cname


# In[106]:


c3.info_c("age")


# In[107]:


c3.info_m()


# In[100]:


c3.info_f()


# ## hierarchical Inheritance

# In[129]:


class Father:
    def __init__(self,fname):
        self.fname=fname
    def info_f(self):
        return f"this a father class"
class Child1(Father):
    def __init__(self,cname1,fname):
        self.cname1=cname1
        super().__init__(fname)
    def info_c1(self,age):
        self.age=5
        return f"this is child1 class {self.age}"
class Child2(Father):
    def __init__(self,cname2,fname):
        self.cname2=cname2
        super().__init__(fname)
    def info_c2(self,age):
        self.age=5
        return f"this is child2 class {self.age}"


# In[130]:


a=Child1("a","b")


# In[131]:


b=Child2("c","d")


# In[132]:


a.fname


# In[133]:


b.fname


# In[134]:


a.info_c1("age")


# In[136]:


b.info_c2("age")


# ## Encapusulation

# ### public variables

# In[146]:


class Student1:
    def __init__(self,name1):
        self.name1=name1
    def info(self):
        return f"{self.name1}"


# In[156]:


class Student2(Student1):
    def __init__(self,name2,name1):
        self.name2=name2
        super().__init__(name1)
    def info_1(self):
        return f"{self.name2}"


# In[157]:


s2= Student2("m","n")


# In[158]:


s2.name1


# In[160]:


s2.info_1()


# ### protected 

# In[166]:


class Student1:
    def __init__(self,name1):
        self._name1=name1    #protected attribute/variable
    def info(self):
        return f"{self.name1}"
class Student2(Student1):
    def __init__(self,name2,name1):
        self.name2=name2
        super().__init__(name1)
    def info_1(self):
        return f"{self.name2}"


# In[167]:


s = Student2("a","s")


# In[168]:


s.name1


# In[169]:


s._name1


# ### private variables

# In[179]:


class Student1:
    def __init__(self,name1,roll):
        self._name1=name1    #protected attribute/variable
        self.__roll=roll       #private "    "    "    "
    def info(self):
        return f"{self.name1}"
class Student2(Student1):
    def __init__(self,name2,name1,roll):
        self.name2=name2
        super().__init__(name1,roll)
    def info_1(self):
        return f"{self.name2}"


# In[180]:


a = Student2("b","c",5)


# In[183]:


a._name1


# In[181]:


a.__roll


# ### Accessing the private variable 

# In[202]:


class Student1:
    def __init__(self,name1,roll):
        self._name1=name1    #protected attribute/variable
        self.__roll=roll      #private "    "    "    "
    def get_roll(self):
        return self.__roll
    def set_roll(self,updateroll):
        self.__roll=updateroll
class Student2(Student1):
    def __init__(self,name2,name1,roll):
        self.name2=name2
        super().__init__(name1,roll)
    def info_1(self):
        return f"{self.name2}"


# In[203]:


q = Student2("s","a",5)


# In[204]:


q.get_roll()


# In[205]:


q.set_roll(30)


# In[207]:


q.get_roll()


# ## Abstraction
# 
# 

# In[216]:


from abc import ABC,abstractmethod


# In[217]:


class Vehicle(ABC):
    @abstractmethod
    def _doorsound(self):
        return ("thud")
    def engine(self):
        return ("Started")


# In[219]:


v = Vehicle()


# In[220]:


v.engine()


# In[221]:


v._doorsound()


# ## polymorphism

# In[222]:


a=10
b=20


# In[224]:


add=a+b
add
print(type(add))


# In[236]:


class Add():
    def __init__(self,number):
        self.number=number
    def __add__(self,other):
        return self.number-other.number


# In[238]:


c= Add(5)
d= Add(10)


# In[239]:


a + b


# In[240]:


class Add():
    def __init__(self,number):
        self.number=number
    def __add__(self,other):
        return self.number*other.number


# In[241]:


e= Add(5)
f= Add(10)


# In[242]:


e+f


# In[1]:


#help("int")


# ## method over riding
# 

# In[17]:


class Parent:
    def __init__(self,name):
        self.name =name
    def info (self):
        return f"this is parent class"
        


# In[18]:


p =parent("sravan")


# In[19]:


p.info()


# In[28]:


class Child(Parent):
    def __init__(self,age,name):
        self.age=age
        super().__init__(name)
    def inf0(self):
        return f"this is child class"


# In[27]:


c = Child(22,"sravn")


# In[22]:


c.age


# In[25]:


c.info()


# ## method over loading
# 

# In[10]:


class Add():
    def add2(self,num1,num2):
        self.num1=num1
        self.num2=num2
        return(num1+num2)
    def add3(self,num1,num2,num3):
        self.num1=num1
        self.num2=num2
        self.num3=num3
        return(num1+num2+num3)
    def add4(self,num1,num2,num3,num4):
        self.num1=num1
        self.num2=num2
        self.num3=num3
        self.num4=num4
        return(num1+num2+num3+num4)


# In[11]:


a=Add()


# In[12]:


a.add2(7,3)


# In[13]:


a.add3(7,3,4)


# In[14]:


a.add4(7,3,4,5)


# In[15]:


a.num2


# In[16]:


class Add():
    def add(self,num1,num2):
        self.num1=num1
        self.num2=num2
        return(num1+num2)
    def add(self,num1,num2,num3):
        self.num1=num1
        self.num2=num2
        self.num3=num3
        return(num1+num2+num3)
    def add(self,num1,num2,num3,num4):
        self.num1=num1
        self.num2=num2
        self.num3=num3
        self.num4=num4
        return(num1+num2+num3+num4)


# In[21]:


a1=Add()


# In[22]:


a1.add(2,3,4)


# In[23]:


import multipledispatch


# In[40]:


class Add():

    @multipledispatch.dispatch(int,int)
    def add(self,num1,num2):
        self.num1=num1
        self.num2=num2
        return(num1+num2)
        
    @multipledispatch.dispatch(int,int,int)
    def add(self,num1,num2,num3):
        self.num1=num1
        self.num2=num2
        self.num3=num3
        return(num1+num2+num3)
        
    @multipledispatch.dispatch(int,int,int,int)
    def add(self,num1,num2,num3,num4):
        self.num1=num1
        self.num2=num2
        self.num3=num3
        self.num4=num4
        return(num1+num2+num3+num4)


# In[41]:


a3=Add()


# In[42]:


a3.add(2,3)


# In[43]:


a3.add(2,3,4)


# In[44]:


a3.add(2,3,4,5)


# In[ ]:




