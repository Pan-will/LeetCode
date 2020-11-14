"""
给你一个数组 orders，表示客户在餐厅中完成的订单，确切地说， orders[i]=[customerNamei,tableNumberi,foodItemi] ，
其中 customerNamei 是客户的姓名，tableNumberi 是客户所在餐桌的桌号，而 foodItemi 是客户点的餐品名称。
请你返回该餐厅的 点菜展示表 。在这张表中，表中第一行为标题，其第一列为餐桌桌号 “Table” ，后面每一列都是按字母顺序排列的餐品名称。
接下来每一行中的项则表示每张餐桌订购的相应餐品数量，第一列应当填对应的桌号，后面依次填写下单的餐品数量。

注意：客户姓名不是点菜展示表的一部分。此外，表中的数据行应该按餐桌桌号升序排列。

示例 1：
输入：orders = [["David","3","Ceviche"],["Corina","10","Beef Burrito"],["David","3","Fried Chicken"],["Carla","5","Water"],["Carla","5","Ceviche"],["Rous","3","Ceviche"]]
输出：[["Table","Beef Burrito","Ceviche","Fried Chicken","Water"],["3","0","2","1","0"],["5","0","1","0","1"],["10","1","0","0","0"]]
解释：
点菜展示表如下所示：
Table,Beef Burrito,Ceviche,Fried Chicken,Water
3    ,0           ,2      ,1            ,0
5    ,0           ,1      ,0            ,1
10   ,1           ,0      ,0            ,0
对于餐桌 3：David 点了 "Ceviche" 和 "Fried Chicken"，而 Rous 点了 "Ceviche"
而餐桌 5：Carla 点了 "Water" 和 "Ceviche"
餐桌 10：Corina 点了 "Beef Burrito"
"""


class Solution(object):
    def displayTable(self, orders):
        """
        :type orders: List[List[str]]
        :rtype: List[List[str]]
        """
        # 返回值
        ans = []
        # 第一趟遍历，listFood统计菜品名称,mydict按桌号统计菜品
        listFood = []
        mydict = {}
        for item in orders:
            table = item[1]
            food = item[2]
            if food not in listFood:
                listFood.append(food)
            if table in mydict.keys():
                mydict[table].append(food)
            else:
                mydict[table] = [food]
        # 菜品按字母升序排
        listFood.sort()
        listFood = ["Table"] + listFood
        # 桌号按升序排
        mylist = sorted(mydict.items(), key=lambda x: int(x[0]), reverse=False)
        ans.append(listFood)
        # 遍历mydict，
        for k, v in mylist:
            temp = [str(k)]
            for food in listFood[1:]:
                if food in v:
                    temp.append(str(v.count(food)))
                else:
                    temp.append(str(0))
            ans.append(temp)
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.displayTable([["David", "3", "Ceviche"], ["Corina", "10", "Beef Burrito"], ["David", "3", "Fried Chicken"],
                          ["Carla", "5", "Water"], ["Carla", "5", "Ceviche"], ["Rous", "3", "Ceviche"]]))
