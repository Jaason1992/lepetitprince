#!/usr/bin/env python
# -*- coding: utf-8 -*-
class student():
    def __init__(self,name,score):
        self.__name=name
        self.__score=score
    def getname(self):
        print 'You name is %s'%self.__name
    def getscore(self):
        print '%s score is %s'%(self.__name,self.__score)

Jason=student('Hong',99)
#Jason('Hong','99')
Jason.getname()
Jason.getscore()

