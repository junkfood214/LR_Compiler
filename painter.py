import math

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import sympy as sym

from myParser import parser


class painter:
    myParser = parser()
    statements = []

    def trans(self, format, ox, oy, ex, ey, angle):
        t_from, t_to, t_step, t_x, t_y = format
        t = np.arange(t_from, t_to, t_step)
        T = sym.symbols('T')
        y = t_y + T - T
        x = t_x + T - T
        y_value = []
        x_value = []
        for i in range(len(t)):
            value = t[i]
            y_value.append(y.evalf(subs={T: value}))
            x_value.append(x.evalf(subs={T: value}))
        # 放缩数据
        et_x = [i * ex for i in x_value]
        et_y = [i * ey for i in y_value]
        # 旋转数据
        between_x = pd.Series(et_x)
        between_y = pd.Series(et_y)
        rx = (between_x * math.cos(angle) + between_y * math.sin(angle))
        ry = (between_y * math.cos(angle) - between_x * math.sin(angle))
        # 平移数据
        fx = (rx + ox).tolist()
        fy = (ry + oy).tolist()
        return et_x, et_y

    def paint(self, string):
        try:
            self.statements = self.myParser.decision(string)
        except Exception as e:
            print(e.args[0])
        if self.statements:
            ox = self.statements[0][0]
            oy = self.statements[0][1]
            # 比例
            ex = self.statements[1][0]
            ey = self.statements[1][1]
            # 角度
            angle = self.statements[2][0]
            print("绘图开始")
            plt.figure(figsize=(5,5))
            plt.axis("equal")
            plt.axis('off')
            for i in range(len(self.statements[3])):
                fx, fy = self.trans(self.statements[3][i], ox, oy, ex, ey, angle)
                plt.plot(fx, fy)
            plt.show()
        else:
            print("绘图失败")
    # sym.plot()


if __name__ == "__main__":
    string = '''
                origin is (100, 100);
                rot is 0;
                scale is (1,1);
                for T from 0 to 150 step 1 draw (t, 0);
                for T from 0 to 150 step 1 draw (0, -t);
                FOR T FROM 0 TO 10 STEP 0.1 DRAW (t,t**2);
                FOR T FROM 0 TO 2*PI STEP PI/100 DRAW (100*sin(t),100*cos(t));
    '''
    paint = painter()
    paint.paint(string)
