class HouseItem:

    def __init__(self,name,arae):
        self.name=name
        self.area=arae

    def __str__(self):
        return "%s 占地 %.2f" % (self.name,self.area)
    
class House:

    def __init__(self,House_type,area):
        self.House_type=House_type
        self.area=area
        self.free_area=area
        self.item_list=[]
    
    def add_item(self,item):
        if(item.area<=self.free_area):
            self.item_list.append(item.name)
            self.free_area=self.free_area-item.area
    
    def __str__(self):
        return ("%s 总面积为%.2f,\n剩余面积为%.2f,\n家具名称列表%s\n" 
                % (self.House_type,self.area,self.free_area,self.item_list))

Xi_ms=HouseItem("席梦思",4)
Yigui=HouseItem("衣柜",2)
Canzhuo=HouseItem("衣柜",1.5)

Beijing_H=House("两室一厅",60)
Beijing_H.add_item(Xi_ms)
Beijing_H.add_item(Yigui)
print(Beijing_H)