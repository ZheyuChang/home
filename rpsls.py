#coding:gbk
"""
��һ��С��Ŀ��Rock-paper-scissors-lizard-Spock
���ߣ�
���ڣ�
"""

import random



# 0 - ʯͷ
# 1 - ʷ����
# 2 - ֽ
# 3 - ����
# 4 - ����

# ����Ϊ�����Ϸ����Ҫ�õ����Զ��庯��

def name_to_number(name):
    if name =="ʯͷ":
        return 0
    if name =="ʷ����":
        return 1
    if name =="��":
        return 2
    if name =="����":
        return 3
    if name =="����":
        return 4
    return name_to_number
    """
    ����Ϸ�����Ӧ����ͬ������
    """

    # ʹ��if/elif/else��佫����Ϸ�����Ӧ����ͬ������
    # ��Ҫ���Ƿ��ؽ��





def number_to_name(number):
    if number ==0:
        return "ʯͷ"
    if number ==1:
        return "ʷ����"
    if number ==2:
        return "��"
    if number ==3:
        return "����"
    if number ==4:
        return "����"
    return number_to_name
    """
    ������ (0, 1, 2, 3, or 4)��Ӧ����Ϸ�Ĳ�ͬ����
    """

    # ʹ��if/elif/else��佫��ͬ��������Ӧ����Ϸ�Ĳ�ͬ����
    # ��Ҫ���Ƿ��ؽ��


election=("ʯͷ","ʷ����","��","����","����")
def rpsls(player_choice):
    """
    �û�����������һ��ѡ�񣬸���RPSLS��Ϸ��������Ļ�������Ӧ�Ľ��

    """
    if player_choice not in election:
        print("Error: No Correct Name")
    else:
        computer_choice=("ʯͷ", "ʷ����", "��", "����", "����")
        # ����Ӯ���б�
        win_list = (["0", "����"], ["4", "��"], ["2", "ʯͷ"], ["0", "����"], ["3", "ʷ����"], ["1", "����"], ["4", "����"], ["3", "��"], ["2", "ʷ����"], ["1", "ʯͷ"])
        # ��������ѡ���ȭ
        mac = random.choice(computer_choice)
        print("�������ѡ��Ϊ��%s" % mac)
        if player_choice == mac:
          print("���ͼ��������һ���ء�")
        elif [player_choice, mac] in win_list:
                # �����Ӯ���б��У�������Ӯ�ˣ���Ҫ��ͼ������˳��Ҫ��Ӯ���б�һ��
          print("��Ӯ��")
        else:
          print("�����Ӯ��")
print("��ӭʹ��RPSLS��Ϸ")
print("����������ѡ��:")
choice_name:str=str(input())
print("----------------")
print("����ѡ��Ϊ:%s"%choice_name)
name_to_number(choice_name)
number_to_name(election)
rpsls(choice_name)


    # ���"-------- "���зָ�
    # ��ʾ�û�������ʾ���û�ͨ�����̽��Լ�����Ϸѡ��������룬�������player_choice

    # ����name_to_number()�������û�����Ϸѡ�����ת��Ϊ��Ӧ���������������player_choice_number

    # ����random.randrange()�Զ�����0-4֮��������������Ϊ��������ѡ�����Ϸ���󣬴������comp_number

    # ����number_to_name()����������������������ת��Ϊ��Ӧ����Ϸ����

    # ����Ļ����ʾ�����ѡ����������

    # ����if/elif/else ��䣬����RPSLS������û�ѡ��ͼ����ѡ������жϣ�������Ļ����ʾ�жϽ��

    # ����û��ͼ����ѡ��һ��������ʾ�����ͼ��������һ���ء�������û���ʤ������ʾ����Ӯ�ˡ�����֮����ʾ�������Ӯ�ˡ�