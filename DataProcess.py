import numpy as np
import matplotlib.pyplot as plt
import sympy as sp

'''
数据拟合
'''
class DataFit:
    def __init__(self, x, y, degree=None):
        self.x = np.array(x, dtype=float)
        self.y = np.array(y, dtype=float)
        self.n_points = len(x)
        # 如果用户指定了阶数，就用指定的；否则走默认规则
        if degree is not None:
            self.chosen_degree = degree
        else:
            self.chosen_degree = min(len(x) - 1, 5) if len(x) > 1 else 1

    def _get_equation_string(self, coeffs):
        # 把多项式系数转换为数学表达式
        terms = []
        deg = len(coeffs) - 1
        for i, c in enumerate(coeffs):
            power = deg - i
            c_fmt = f"{c:.3f}"
            if power == 0:
                terms.append(f"{c_fmt}")
            elif power == 1:
                terms.append(f"{c_fmt}·x")
            else:
                terms.append(f"{c_fmt}·x^{power}")
        return " + ".join(terms)

    def Visualize(self):
        # 对数据进行排序，防止曲线乱跳
        sorted_idx = np.argsort(self.x)
        x_sorted = self.x[sorted_idx]
        y_sorted = self.y[sorted_idx]

        coeffs = np.polyfit(x_sorted, y_sorted, self.chosen_degree)
        poly_func = np.poly1d(coeffs)

        # 用更密集的采样点生成平滑曲线
        x_dense = np.linspace(x_sorted.min(), x_sorted.max(), 500)
        y_fit = poly_func(x_dense)

        equation_str = self._get_equation_string(coeffs)

        plt.scatter(self.x, self.y, color="blue", label="Observed data")
        plt.plot(x_dense, y_fit, "r-", label=f"Fitted curve (degree={self.chosen_degree})")
        plt.xlabel("x")
        plt.ylabel("y")
        plt.legend()
        plt.title("Polynomial Fitting with Equation")
        plt.grid(True)
        # 在图的左上角显示拟合方程
        plt.text(0.05, 0.95, f"y = {equation_str}", transform=plt.gca().transAxes,
                 fontsize=9, verticalalignment='top', bbox=dict(facecolor='white', alpha=0.5))
        plt.show()

def GetRawCoords():
    #读取原始坐标
    try:
        raw_x = input("Enter x coordinates separated by spaces: ").strip()
        raw_y = input("Enter y coordinates separated by spaces: ").strip()
        if not raw_x or not raw_y:
            print(">>> No data entered.")
            return None, None
        x = list(map(float, raw_x.split()))
        y = list(map(float, raw_y.split()))
        if len(x) != len(y):
            print(">>> x and y must have the same number of points!")
            return None, None
        return x, y
    except ValueError:
        print(">>> Invalid number format!")
        return None, None

'''
数据处理
'''
class DataProc:
    def __init__(self, data):
        self.data = np.array(data, dtype=float)

    def GetMean(self):
        return np.mean(self.data)

    def GetStdSample(self):
        if self.data.size < 2:
            print(">>> At least two data points are needed for sample std!")
            return float("nan")
        return np.std(self.data, ddof=1)  # 样本标准差

    def GetUA(self):
        if self.data.size < 2:
            return float("nan")
        return self.GetStdSample() / np.sqrt(self.data.size)  # A 类不确定度

    def GetUB(self, resolution):
        return resolution / np.sqrt(3)  # B 类不确定度

    def GetUncertainty(self, resolution):
        u_a = self.GetUA()
        u_b = self.GetUB(resolution)
        return np.sqrt(u_a**2 + u_b**2)  # 合成标准不确定度
    
def GetYwithX():
    # 根据 x 和表达式生成 y
    expr = input("Enter the expression for y in terms of x: ").strip()
    x_sym = sp.symbols('x')
    try:
        y_func = sp.sympify(expr)
        x = list(map(float, input("Enter x values separated by spaces: ").strip().split()))
        y = [float(y_func.subs(x_sym, val)) for val in x]
        return x, y
    except (sp.SympifyError, ValueError):
        print(">>> Invalid expression!")
        return None, None

def GetRawData():
    #读取原始数据
    try:
        raw = input("Enter data points separated by spaces: ").strip()
        if not raw:
            print(">>> No data entered.")
            return None, None
        data = list(map(float, raw.split()))
        res = input("Enter instrument resolution (if any, default 0): ").strip()
        resolution = float(res) if res else 0.0
        return data, resolution
    except ValueError:
        print(">>> Invalid number format!")
        return None, None

def main():
    while True:
        menu = (
        "Data Processing Module\n"
        "[0] Exit\n"
        "[1] Process Data\n"
        "[2] Fit Data\n"
        )
        print(menu)
        try:
            sel = int(input("Enter your choice: "))
        except ValueError:
            print(">>> Please enter an integer!")
            continue

        if sel == 0:
            break
        elif sel == 1:
            data, resolution = GetRawData()
            if data is None:
                continue
            dp = DataProc(data)
            mean = dp.GetMean()
            std_sample = dp.GetStdSample()
            u_a = dp.GetUA()
            u_b = dp.GetUB(resolution)
            uncertainty = dp.GetUncertainty(resolution)

            print("Results:")
            print(f"  Mean                        : {mean:.4f}")
            print(f"  Sample Standard Deviation   : {std_sample:.4f}")
            print(f"  Uncertainty A (std error)   : {u_a:.4f}")
            print(f"  Uncertainty B (resolution)  : {u_b:.4f}")
            print(f"  Combined Uncertainty        : {uncertainty:.4f}\n")
        elif sel == 2:
            print("Choose input method:"
                  "\n[1] Enter (x, y) pairs"
                  "\n[2] Enter x values and expression for y"
                  "\n[0] Return to main menu"
                  )
            try:
                method = int(input("Enter your choice: "))
            except ValueError:
                print(">>> Please enter an integer!")
                continue
            if method == 0:
                continue
            elif method == 1:
                x, y = GetRawCoords()
                if x is None or y is None:
                    continue
            elif method == 2:
                x, y = GetYwithX()
                if x is None or y is None:
                    print(">>> Error in generating y values.")
                    continue
            else:
                print(">>> Invalid choice.")
                continue

            # 这里加阶数选择
            deg_in = input("Enter polynomial degree (press Enter for default): ").strip()
            if deg_in:
                try:
                    degree = int(deg_in)
                    df = DataFit(x, y, degree=degree)
                except ValueError:
                    print(">>> Invalid degree input, using default.")
                    df = DataFit(x, y)
            else:
                df = DataFit(x, y)

            df.Visualize()
        else:
            print(">>> Invalid choice, please try again.")

if __name__ == "__main__":
    main()




