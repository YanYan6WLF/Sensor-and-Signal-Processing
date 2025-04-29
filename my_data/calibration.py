import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import numpy as np

import pandas as pd

# 读取 CSV 文件
file_path1 = './calibrated_magnetic_field_in_XYZ_1.csv'
file_path2 = './calibrated_magnetic_field_in_XYZ_2.csv'
file_path3 = './calibrated_magnetic_field_in_XYZ_3.csv'
file_path4 = './calibrated_magnetic_field_in_XYZ_4.csv'

df1 = pd.read_csv(file_path1)
df2 = pd.read_csv(file_path2)
df3 = pd.read_csv(file_path3)
df4 = pd.read_csv(file_path4)

# 查看数据的前几行
print(df1.head())
print(df1.columns)
# 按列访问数据
#t10=df.iloc[:,0]
#t10=df1['Time (s)']
Bx2=df2['Bx']
By2=df2['By']
Bz2=df2['Bz']
#B2=[Bx2,By2,Bz2]
B2 = np.sqrt(Bx2**2 + By2**2 + Bz2**2)
B2 = [0,-B2,0]
#规定正电流的方向为正


Bx3=df3['Bx']
By3=df3['By']
Bz3=df3['Bz']
#B3=[Bx3,By3,Bz3]
B3 = np.sqrt(Bx3**2 + By3**2 + Bz3**2)
B3 = [0,B3,0]


Bx4=df4['Bx']
By4=df4['By']
Bz4=df4['Bz']
#B4=[Bx4,By4,Bz4]
B4 = np.sqrt(Bx4**2 + By4**2 + Bz4**2)
B4 = [0,B4,0]


Bx1=df1['Bx']
By1=df1['By']
Bz1=df1['Bz']
#B1=[Bx1,By1,Bz1]
B1 = np.sqrt(Bx1**2 + By1**2 + Bz1**2)
B1 = [0,-B1,0]



#offsetX1 = t11[t10 < 1].mean() #假设 t10 和 t11 是 pandas 中的 Series 对象

#t11_smoothed = t11_calibrated.rolling(window=windowSize, center=True).mean()
#Bx1 = np.mean(t11_calibrated[(t10 > 5) & (t10 < 10)])

def draw_helmholtz_coils(ax, coil_radius, coil_spacing):
    theta = np.linspace(0, 2 * np.pi, 100)
    x = coil_radius * np.cos(theta)
    z = coil_radius * np.sin(theta)
    
    # Left coil
    y1 = np.full_like(x, -coil_spacing / 2)
    ax.plot(x, y1, z, 'r', label='Helmholtz Coil (Left)', linewidth=2)
    
    # Right coil
    y2 = np.full_like(x, coil_spacing / 2)
    ax.plot(x, y2, z, 'b', label='Helmholtz Coil (Right)', linewidth=2)

def draw_realistic_phone(ax):
    # Phone dimensions (in mm)
    phone_length = 100  # mm
    phone_width = 60    # mm
    phone_thickness = 10  # mm
    bezel_thickness = 5   # mm
    
    # Phone base coordinates
    base = [
        [-phone_width / 2, -phone_length / 2, -phone_thickness / 2],  # Bottom face
        [phone_width / 2, -phone_length / 2, -phone_thickness / 2],
        [phone_width / 2, phone_length / 2, -phone_thickness / 2],
        [-phone_width / 2, phone_length / 2, -phone_thickness / 2],
    ]
    base = np.array(base)
    
    # Top face coordinates
    top = base.copy()
    top[:, 2] = phone_thickness / 2

    # Screen coordinates (slightly inset)
    screen = [
        [-phone_width / 2 + bezel_thickness, -phone_length / 2 + bezel_thickness, phone_thickness / 2],
        [phone_width / 2 - bezel_thickness, -phone_length / 2 + bezel_thickness, phone_thickness / 2],
        [phone_width / 2 - bezel_thickness, phone_length / 2 - bezel_thickness, phone_thickness / 2],
        [-phone_width / 2 + bezel_thickness, phone_length / 2 - bezel_thickness, phone_thickness / 2],
    ]
    screen = np.array(screen)
    
    # Define faces for the phone and screen
    phone_faces = [
        [base[0], base[1], base[2], base[3]],  # Bottom
        [top[0], top[1], top[2], top[3]],      # Top
        [base[0], base[1], top[1], top[0]],    # Side faces
        [base[1], base[2], top[2], top[1]],
        [base[2], base[3], top[3], top[2]],
        [base[3], base[0], top[0], top[3]],
    ]
    screen_faces = [
        [screen[0], screen[1], screen[2], screen[3]]
    ]
    
    # Add the phone to the plot
    ax.add_collection3d(Poly3DCollection(phone_faces, color='gray', alpha=0.8, edgecolor='k', label='Phone Body'))
    ax.add_collection3d(Poly3DCollection(screen_faces, color='black', alpha=0.9, edgecolor='k', label='Phone Screen'))

def plot_realistic_model(B_vector1,B_vector2,title):
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111, projection='3d')


    # Helmholtz coil parameters
    coil_radius = 150  # mm
    coil_spacing = 150  # mm

    # Draw Helmholtz coils
    draw_helmholtz_coils(ax, coil_radius, coil_spacing)

    # Draw realistic phone
    draw_realistic_phone(ax)

    # Add magnetic field vector
    origin = [0, 0, 0]
    #它解包了元组或列表中的元素，将它们逐一传递给函数的参数。
    ax.quiver(*origin, *B_vector1, color='gold', linewidth=2, arrow_length_ratio=0.2, label='Magnetic Field Vector [negative current]')
    ax.quiver(*origin, *B_vector2, color='c', linewidth=2, arrow_length_ratio=0.2, label='Magnetic Field Vector [positive current]')

    # Set labels and aspect
    ax.set_xlabel('X-axis (mm)')
    ax.set_ylabel('Y-axis (mm)')
    ax.set_zlabel('Z-axis (mm)')
    ax.set_xlim([-200, 200])
    ax.set_ylim([-700, 700])
    ax.set_zlim([-200, 200])
    ax.legend()
    ax.set_title(title)

    plt.show()

plot_realistic_model(B1,B4,title='Realistic Model of Phone in Helmholtz Coil with Magnetic Field [current abs=0.8561 A]')
plot_realistic_model(B2,B3,title='Realistic Model of Phone in Helmholtz Coil with Magnetic Field [current abs=0.4335 A]')

