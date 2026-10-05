# COMP4139 Machine Learning

独立 Python 3.12 开发环境。

- src/：Python 源代码
- notebook/：Jupyter Notebook
- data/：数据
- outputs/：图表和运行结果
- tests/：测试代码

在 VS Code 中打开本目录，通过 Python: Select Interpreter 选择 .venv\Scripts\python.exe。

验证环境：
```powershell
.\.venv\Scripts\python.exe -c "import sys; print(sys.executable); print(sys.prefix != sys.base_prefix)"
```

安装课程需要的库后，更新依赖清单：
```powershell
.\.venv\Scripts\python.exe -m pip freeze > requirements.txt
```

当前未安装第三方课程库；requirements.txt 为空。后续根据课程材料安装。
