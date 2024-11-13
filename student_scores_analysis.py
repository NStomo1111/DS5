import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

# データの生成
np.random.seed(42)
num_students = 50
subjects = ['Math', 'Science', 'English', 'History', 'Art']

scores = pd.DataFrame({
    'Student ID': [f'Student {i+1}' for i in range(num_students)],
    'Math': np.random.randint(50, 101, num_students),
    'Science': np.random.randint(50, 101, num_students),
    'English': np.random.randint(50, 101, num_students),
    'History': np.random.randint(50, 101, num_students),
    'Art': np.random.randint(50, 101, num_students)
})

# 棒グラフの作成
plt.figure(figsize=(12, 6))
scores.set_index('Student ID').plot(kind='bar')
plt.title('Scores by Student')
plt.xlabel('Student ID')
plt.ylabel('Scores')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('bar_chart_scores.png')
plt.close()

# 散布図の作成
plt.figure(figsize=(10, 8))
sns.pairplot(scores.drop('Student ID', axis=1), diag_kind='kde')
plt.suptitle('Subject Correlation Scatter Plots', y=1.02)
plt.tight_layout()
plt.savefig('scatter_plot_correlations.png')
plt.close()

# 主成分分析
pca = PCA(n_components=2)
scaler = StandardScaler()
scaled_scores = scaler.fit_transform(scores.drop('Student ID', axis=1))
pca_result = pca.fit_transform(scaled_scores)

plt.figure(figsize=(8, 6))
plt.scatter(pca_result[:, 0], pca_result[:, 1], alpha=0.7)
plt.title('PCA of Student Scores')
plt.xlabel('Principal Component 1')
plt.ylabel('Principal Component 2')
plt.grid(True)
plt.savefig('pca_plot.png')
plt.close()

print("グラフが生成されました。")
