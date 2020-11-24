#coding:gbk
"""
第一个小项目：Rock-paper-scissors-lizard-Spock
作者：
日期：
"""

import random



# 0 - 石头
# 1 - 史波克
# 2 - 纸
# 3 - 蜥蜴
# 4 - 剪刀

# 以下为完成游戏所需要用到的自定义函数

def name_to_number(name):
    if name =="石头":
        return 0
    if name =="史波克":
        return 1
    if name =="布":
        return 2
    if name =="蜥蜴":
        return 3
    if name =="剪刀":
        return 4
    return name_to_number
    """
    将游戏对象对应到不同的整数
    """

    # 使用if/elif/else语句将各游戏对象对应到不同的整数
    # 不要忘记返回结果





def number_to_name(number):
    if number ==0:
        return "石头"
    if number ==1:
        return "史波克"
    if number ==2:
        return "布"
    if number ==3:
        return "蜥蜴"
    if number ==4:
        return "剪刀"
    return number_to_name
    """
    将整数 (0, 1, 2, 3, or 4)对应到游戏的不同对象
    """

    # 使用if/elif/else语句将不同的整数对应到游戏的不同对象
    # 不要忘记返回结果


election=("石头","史波克","布","蜥蜴","剪刀")
def rpsls(player_choice):
    """
    用户玩家任意给出一个选择，根据RPSLS游戏规则，在屏幕上输出对应的结果

    """
    if player_choice not in election:
        print("Error: No Correct Name")
    else:
        computer_choice=("石头", "史波克", "布", "蜥蜴", "剪刀")
        # 定义赢的列表
        win_list = (["0", "剪刀"], ["4", "布"], ["2", "石头"], ["0", "蜥蜴"], ["3", "史波克"], ["1", "剪刀"], ["4", "蜥蜴"], ["3", "布"], ["2", "史波克"], ["1", "石头"])
        # 计算机随机选择出拳
        mac = random.choice(computer_choice)
        print("计算机的选择为：%s" % mac)
        if player_choice == mac:
          print("您和计算基础的一样呢。")
        elif [player_choice, mac] in win_list:
                # 如果在赢的列表中，代表你赢了，主要你和计算机的顺序要和赢的列表一样
          print("您赢了")
        else:
          print("计算机赢了")
print("欢迎使用RPSLS游戏")
print("请输入您的选择:")
choice_name:str=str(input())
print("----------------")
print("您的选择为:%s"%choice_name)
name_to_number(choice_name)
number_to_name(election)
rpsls(choice_name)


    # 输出"-------- "进行分割
    # 显示用户输入提示，用户通过键盘将自己的游戏选择对象输入，存入变量player_choice

    # 调用name_to_number()函数将用户的游戏选择对象转换为相应的整数，存入变量player_choice_number

    # 利用random.randrange()自动产生0-4之间的随机整数，作为计算机随机选择的游戏对象，存入变量comp_number

    # 调用number_to_name()函数将计算机产生的随机数转换为对应的游戏对象

    # 在屏幕上显示计算机选择的随机对象

    # 利用if/elif/else 语句，根据RPSLS规则对用户选择和计算机选择进行判断，并在屏幕上显示判断结果

    # 如果用户和计算机选择一样，则显示“您和计算机出的一样呢”，如果用户获胜，则显示“您赢了”，反之则显示“计算机赢了”