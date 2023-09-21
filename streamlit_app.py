import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

# Streamlitアプリのタイトル
st.title("宇宙デブリの軌道計算アプリ")

# 宇宙デブリの初期位置（x, y, z） [m]
initial_position_x = st.number_input("初期X座標 [m]", value=100000)
initial_position_y = st.number_input("初期Y座標 [m]", value=100000)
initial_position_z = st.number_input("初期Z座標 [m]", value=0)

# 宇宙デブリの初期速度（vx, vy, vz） [m/s]
initial_velocity_x = st.number_input("初期X速度 [m/s]", value=1000)
initial_velocity_y = st.number_input("初期Y速度 [m/s]", value=0)
initial_velocity_z = st.number_input("初期Z速度 [m/s]", value=0)

# シミュレーションの時間範囲
simulation_time = st.number_input("シミュレーション時間（秒）", value=86400)

# 地球の質量 [kg]
earth_mass = 5.972e24

# 宇宙デブリの質量 [kg]（小さなデブリの場合、無視することが一般的）
debris_mass = 1.0

def debris_motion(t, state):
    x, y, z, vx, vy, vz = state
    r = np.sqrt(x**2 + y**2 + z**2)
    gravitational_force = -earth_mass / r**3 * np.array([x, y, z])
    dxdt = vx
    dydt = vy
    dzdt = vz
    dvxdt = gravitational_force[0] / debris_mass
    dvydt = gravitational_force[1] / debris_mass
    dvzdt = gravitational_force[2] / debris_mass
    return [dxdt, dydt, dzdt, dvxdt, dvydt, dvzdt]

initial_state = [initial_position_x, initial_position_y, initial_position_z,
                 initial_velocity_x, initial_velocity_y, initial_velocity_z]

# 解を計算
solution = solve_ivp(debris_motion, (0, simulation_time), initial_state, t_eval=np.linspace(0, simulation_time, 1000))

# 結果をプロット
fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(111, projection='3d')
ax.plot(solution.y[0], solution.y[1], solution.y[2])
ax.set_xlabel('X軸 [m]')
ax.set_ylabel('Y軸 [m]')
ax.set_zlabel('Z軸 [m]')
ax.set_title('宇宙デブリの軌道')
st.pyplot(fig)
