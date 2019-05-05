# -*- coding: utf-8 -*-
import sublime
import sublime_plugin
from datetime import datetime
import re ,time

# Type 'now' 然后按 <tab> 转为当前时间 年-月-日 时:分:秒.
# 'tsnow' + <tab> 显示当前时间戳
# 年-月-日-时-分-秒 转为时间戳
def changeTime(t):
    #patten1 匹配10为整数时间戳
    pattern1 = re.compile('^\d{10}')
    match = pattern1.match(t)
    #pattern2 匹配d20141220235959这样的时间字符串
    pattern2 = re.compile('^(\d{4})-(\d{1,2})-(\d{1,2}) (\d{1,2}):(\d{1,2}):(\d{1,2})')
    match2 = pattern2.match(t)

    if match:
        timeStamp = int(match.group(0))
        timeArray = time.localtime(timeStamp)
        val = time.strftime('%Y-%m-%d %H:%M:%S',timeArray)
    elif match2:
        timeStr = match2.group(1) + '-' + match2.group(2) + '-' + match2.group(3) +' ' + match2.group(4)+ ':' + match2.group(5)+ ':' + match2.group(6)
        timeArray = time.strptime(timeStr, "%Y-%m-%d %H:%M:%S")
        val = str(time.mktime(timeArray)).split('.')[0]
    else:
        val = None

    return val;

class time_formatCommand(sublime_plugin.TextCommand):
    """Expand `now`, `tsnow`
    """

    def run(self,edit):
        # 当前视图
        view = self.view
        # 选中部分
        sels = view.sel()
        for sel in sels:
            selStr = view.substr(sel)
            timeStr = changeTime(selStr)
            if timeStr is not None:
                try:
                    view.replace(edit,sel,timeStr)
                except:
                    pass


