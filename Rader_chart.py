import matplotlib.pyplot as plt
import numpy as np

categories = ['Accurancy', 'Collision', 'Trajectory_completion', 'Time_Task Completion', 'Actuator_Saturation']
values = [4, 5, 3, 4, 2]

angles = np.linspace(0, 2 * np.pi, len(categories), endpoint=False).tolist()
values += values[:1]
angles += angles[:1]

fig, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(polar=True))
ax.fill(angles, values, color='cyan', alpha=0.25)
ax.plot(angles, values, color='blue', linewidth=2, linestyle='--')

ax.set_yticks([1, 2, 3, 4, 5])
ax.set_yticklabels(["1", "2", "3", "4", "5"], color="grey", size=10)
ax.set_xticks(angles[:-1])
ax.set_xticklabels(categories, color='darkblue', fontsize=12, fontweight='bold')
plt.title('Welcome to Dipsagar Radar Chart', size=15, color='darkblue', weight='bold')
ax.spines['polar'].set_visible(False)  
ax.grid(color='gray', linestyle='--', linewidth=0.5)
ax.set_facecolor('#f0f0f0') 
plt.show()
