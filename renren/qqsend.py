#coding:UTF-8
from qqbot import _bot as bot

def sendMsgToGroup(msg,groupList,bot):
    for group in groupList:
        bg=bot.List('group', group)
        if bg is not None:
            bot.SendTo(bg[0],msg)

def sendMsgToBuddy(msg,buddyList,bot):
    pass

def main(bot):
    groupMsg=''
    buddyMsg='123'
    # with open('./qq.txt','r') as fr:
    #     qqGroup=fr.readline().strip()
    #     qqBuddy=fr.readline().strip()
    # qqGroupList=qqGroup.split(',')
    # qqBuddyList=qqBuddy.split(',')
    # sendMsgToGroup(groupMsg,qqGroupList,bot)
    # sendMsgToBuddy(buddyMsg,'1084933098',bot)
    bg=bot.List('buddy', '1084933098')
    bot.SendTo(bg[0],'123')


if __name__=='__main__':
    bot.Login(['-q', '1808163167'])
    main(bot)
    # print bot.buddy