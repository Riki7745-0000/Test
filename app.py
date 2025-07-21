<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>零件测试管理系统</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <link href="https://cdn.jsdelivr.net/npm/font-awesome@4.7.0/css/font-awesome.min.css" rel="stylesheet">
    <script>
        tailwind.config = {
            theme: {
                extend: {
                    colors: {
                        primary: '#165DFF',
                        secondary: '#0FC6C2',
                        accent: '#722ED1',
                        success: '#00B42A',
                        warning: '#FF7D00',
                        danger: '#F53F3F',
                        info: '#86909C',
                        light: '#F2F3F5',
                        dark: '#1D2129',
                    },
                    fontFamily: {
                        sans: ['Inter', 'system-ui', 'sans-serif'],
                    },
                }
            }
        }
    </script>
    <style type="text/tailwindcss">
        @layer utilities {
            .content-auto {
                content-visibility: auto;
            }
            .card-shadow {
                box-shadow: 0 4px 20px rgba(0, 0, 0, 0.08);
            }
            .table-shadow {
                box-shadow: 0 2px 12px rgba(0, 0, 0, 0.04);
            }
            .btn-hover {
                @apply transition-all duration-300 hover:shadow-lg transform hover:-translate-y-0.5;
            }
        }
    </style>
</head>
<body class="bg-gray-50 min-h-screen">
    <div class="container mx-auto px-4 py-6">
        <!-- 标题栏 -->
        <header class="mb-6">
            <h1 class="text-[clamp(1.5rem,3vw,2.5rem)] font-bold text-primary flex items-center">
                <i class="fa fa-cogs mr-3"></i>零件测试管理系统
            </h1>
            <p class="text-gray-500 mt-1">高效管理零件测试流程，提升工作效率</p>
        </header>

        <!-- 主内容区 -->
        <main class="space-y-6">
            <!-- 录入新任务卡片 -->
            <section class="bg-white rounded-xl p-6 card-shadow">
                <h2 class="text-xl font-semibold text-dark mb-4 flex items-center">
                    <i class="fa fa-plus-circle text-primary mr-2"></i>录入新任务
                </h2>
                <form id="taskForm" class="grid grid-cols-1 md:grid-cols-3 gap-6">
                    <!-- 左侧：基本信息 -->
                    <div class="space-y-4">
                        <div>
                            <label for="lims_no" class="block text-sm font-medium text-gray-700 mb-1">LIMS号</label>
                            <input type="text" id="lims_no" name="lims_no" class="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-primary/50 focus:border-primary transition">
                        </div>
                        <div>
                            <label for="location_no" class="block text-sm font-medium text-gray-700 mb-1">库位号</label>
                            <input type="text" id="location_no" name="location_no" class="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-primary/50 focus:border-primary transition">
                        </div>
                        <div>
                            <label for="register_time" class="block text-sm font-medium text-gray-700 mb-1">登记时间</label>
                            <input type="date" id="register_time" name="register_time" value="" class="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-primary/50 focus:border-primary transition">
                        </div>
                    </div>

                    <!-- 中间：测试项 -->
                    <div class="space-y-4">
                        <div>
                            <label for="test_item1" class="block text-sm font-medium text-gray-700 mb-1">测试项1</label>
                            <select id="test_item1" name="test_item1" class="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-primary/50 focus:border-primary transition">
                                <option value="冷凝水">冷凝水</option>
                                <option value="PV1200">PV1200</option>
                                <option value="PV1303">PV1303</option>
                            </select>
                        </div>
                        <div>
                            <label for="test_item2" class="block text-sm font-medium text-gray-700 mb-1">测试项2</label>
                            <select id="test_item2" name="test_item2" class="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-primary/50 focus:border-primary transition">
                                <option value="90℃">90℃</option>
                                <option value="cream resist">cream resist</option>
                            </select>
                        </div>
                        <div>
                            <label for="test_item3" class="block text-sm font-medium text-gray-700 mb-1">测试项3</label>
                            <select id="test_item3" name="test_item3" class="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-primary/50 focus:border-primary transition">
                                <option value="存放类测试">存放类测试</option>
                                <option value="摩擦类测试">摩擦类测试</option>
                            </select>
                        </div>
                    </div>

                    <!-- 右侧：委托信息 -->
                    <div class="space-y-4">
                        <div>
                            <label for="client" class="block text-sm font-medium text-gray-700 mb-1">委托人</label>
                            <select id="client" name="client" class="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-primary/50 focus:border-primary transition">
                                <option value="WX">WX</option>
                                <option value="其他固定人员">其他固定人员</option>
                            </select>
                        </div>
                        <div>
                            <label for="trustee" class="block text-sm font-medium text-gray-700 mb-1">被委托人</label>
                            <select id="trustee" name="trustee" class="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-primary/50 focus:border-primary transition">
                                <option value="XYF">XYF</option>
                                <option value="其他固定人员">其他固定人员</option>
                            </select>
                        </div>
                        <div class="flex items-end">
                            <button type="button" id="generateTaskBtn" class="w-full bg-primary hover:bg-primary/90 text-white font-medium py-2 px-4 rounded-md transition-all duration-300 flex items-center justify-center btn-hover">
                                <i class="fa fa-plus-circle mr-2"></i>生成测试项
                            </button>
                        </div>
                    </div>
                </form>
            </section>

            <!-- 测试单表格卡片 -->
            <section class="bg-white rounded-xl p-6 card-shadow">
                <h2 class="text-xl font-semibold text-dark mb-4 flex items-center">
                    <i class="fa fa-table text-primary mr-2"></i>测试单表格
                </h2>
                <div class="overflow-x-auto table-shadow rounded-lg">
                    <table class="min-w-full divide-y divide-gray-200">
                        <thead class="bg-gray-50">
                            <tr>
                                <th scope="col" class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">序号</th>
                                <th scope="col" class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">LIMS号</th>
                                <th scope="col" class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">零件号</th>
                                <th scope="col" class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">是否为总成</th>
                                <th scope="col" class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">材料</th>
                                <th scope="col" class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">零件位置</th>
                                <th scope="col" class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">被委托人</th>
                                <th scope="col" class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">委托人</th>
                                <th scope="col" class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">登记时间</th>
                                <th scope="col" class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">预计完成时间</th>
                                <th scope="col" class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">实验项目</th>
                            </tr>
                        </thead>
                        <tbody id="taskTableBody" class="bg-white divide-y divide-gray-200">
                            <!-- 数据将通过JavaScript动态加载 -->
                            <tr>
                                <td colspan="11" class="px-6 py-10 text-center text-gray-500">
                                    <div class="flex flex-col items-center">
                                        <i class="fa fa-spinner fa-spin text-2xl mb-3 text-primary"></i>
                                        <p>正在加载数据...</p>
                                    </div>
                                </td>
                            </tr>
                        </tbody>
                    </table>
                </div>
            </section>

            <!-- 任务统计卡片 -->
            <section class="bg-white rounded-xl p-6 card-shadow">
                <h2 class="text-xl font-semibold text-dark mb-4 flex items-center">
                    <i class="fa fa-bar-chart text-primary mr-2"></i>任务统计
                </h2>
                <div id="statsContainer" class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
                    <!-- 数据将通过JavaScript动态加载 -->
                    <div class="col-span-full flex justify-center py-10">
                        <div class="flex flex-col items-center">
                            <i class="fa fa-spinner fa-spin text-2xl mb-3 text-primary"></i>
                            <p>正在加载统计数据...</p>
                        </div>
                    </div>
                </div>
            </section>
        </main>

        <!-- 页脚 -->
        <footer class="mt-12 text-center text-gray-500 text-sm py-4 border-t border-gray-200">
            <p>© 2025 零件测试管理系统 | 版本 1.0.0</p>
        </footer>
    </div>

    <!-- 模态框 -->
    <div id="messageModal" class="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center z-50 hidden">
        <div class="bg-white rounded-lg p-6 max-w-md w-full mx-4 transform transition-all">
            <div id="modalIcon" class="w-16 h-16 mx-auto mb-4 flex items-center justify-center rounded-full text-white text-2xl"></div>
            <h3 id="modalTitle" class="text-xl font-semibold text-center mb-2"></h3>
            <p id="modalMessage" class="text-gray-600 text-center mb-6"></p>
            <button id="modalCloseBtn" class="w-full bg-primary hover:bg-primary/90 text-white font-medium py-2 px-4 rounded-md transition-all duration-300 btn-hover">
                确定
            </button>
        </div>
    </div>

    <script>
        // 设置默认日期为今天
        document.addEventListener('DOMContentLoaded', function() {
            const today = new Date().toISOString().split('T')[0];
            document.getElementById('register_time').value = today;
            
            // 加载数据
            loadTasks();
            loadStats();
            
            // 绑定事件
            document.getElementById('generateTaskBtn').addEventListener('click', generateTask);
            document.getElementById('modalCloseBtn').addEventListener('click', closeModal);
        });
        
        // 加载任务数据
        function loadTasks() {
            fetch('/api/tasks')
                .then(response => response.json())
                .then(data => {
                    const tableBody = document.getElementById('taskTableBody');
                    tableBody.innerHTML = '';
                    
                    if (data.length === 0) {
                        tableBody.innerHTML = `
                            <tr>
                                <td colspan="11" class="px-6 py-10 text-center text-gray-500">
                                    <div class="flex flex-col items-center">
                                        <i class="fa fa-inbox text-3xl mb-3 text-gray-400"></i>
                                        <p>暂无任务数据</p>
                                    </div>
                                </td>
                            </tr>
                        `;
                        return;
                    }
                    
                    data.forEach((task, index) => {
                        const row = document.createElement('tr');
                        row.className = index % 2 === 0 ? 'bg-white' : 'bg-gray-50';
                        
                        // 计算预计完成时间
                        const dueDate = new Date(task.register_time);
                        dueDate.setDate(dueDate.getDate() + 17);
                        const dueDateStr = dueDate.toISOString().split('T')[0];
                        
                        // 实验项目
                        const experimentItem = `${task.test_item1}, ${task.test_item2}, ${task.test_item3}`;
                        
                        row.innerHTML = `
                            <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-500">${index + 1}</td>
                            <td class="px-6 py-4 whitespace-nowrap text-sm font-medium text-gray-900">${task.lims_no}</td>
                            <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-500">${task.part_no}</td>
                            <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-500">${task.is_total}</td>
                            <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-500">${task.material}</td>
                            <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-500">${task.part_location}</td>
                            <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-500">${task.trustee}</td>
                            <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-500">${task.client}</td>
                            <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-500">${task.register_time}</td>
                            <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-500">${dueDateStr}</td>
                            <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-500">${experimentItem}</td>
                        `;
                        
                        tableBody.appendChild(row);
                    });
                })
                .catch(error => {
                    console.error('Error loading tasks:', error);
                    showMessage('错误', '加载任务数据失败，请稍后重试', 'error');
                });
        }
        
        // 加载统计数据
        function loadStats() {
            fetch('/api/stats')
                .then(response => response.json())
                .then(data => {
                    const statsContainer = document.getElementById('statsContainer');
                    statsContainer.innerHTML = '';
                    
                    if (data.length === 0) {
                        statsContainer.innerHTML = `
                            <div class="col-span-full flex justify-center py-10">
                                <div class="flex flex-col items-center">
                                    <i class="fa fa-inbox text-3xl mb-3 text-gray-400"></i>
                                    <p>暂无统计数据</p>
                                </div>
                            </div>
                        `;
                        return;
                    }
                    
                    data.forEach(personStats => {
                        const pending = personStats.total - personStats.completed;
                        
                        const card = document.createElement('div');
                        card.className = 'bg-white rounded-lg p-5 shadow-sm border border-gray-200 transition-all hover:shadow-md';
                        
                        card.innerHTML = `
                            <div class="flex justify-between items-center mb-4">
                                <h3 class="text-lg font-semibold text-gray-800">${personStats.person}</h3>
                                <span class="bg-primary/10 text-primary text-xs font-medium px-2.5 py-0.5 rounded">
                                    ${pending > 0 ? '进行中' : '已完成'}
                                </span>
                            </div>
                            <div class="space-y-3">
                                <div class="flex justify-between items-center">
                                    <span class="text-sm text-gray-600">总任务数</span>
                                    <span class="text-sm font-medium text-gray-900">${personStats.total}</span>
                                </div>
                                <div class="flex justify-between items-center">
                                    <span class="text-sm text-gray-600">已完成</span>
                                    <span class="text-sm font-medium text-green-600">${personStats.completed}</span>
                                </div>
                                <div class="flex justify-between items-center">
                                    <span class="text-sm text-gray-600">待完成</span>
                                    <span class="text-sm font-medium text-orange-500">${pending}</span>
                                </div>
                                <div class="mt-4 flex space-x-3">
                                    <button class="flex-1 bg-green-50 hover:bg-green-100 text-green-700 px-3 py-2 rounded-md text-sm font-medium transition-all duration-300" 
                                            onclick="updateCompleted('${personStats.person}', ${personStats.completed + 1})">
                                        <i class="fa fa-plus-circle mr-1"></i> 完成
                                    </button>
                                    <button class="flex-1 bg-red-50 hover:bg-red-100 text-red-700 px-3 py-2 rounded-md text-sm font-medium transition-all duration-300"
                                            onclick="updateCompleted('${personStats.person}', ${personStats.completed - 1})">
                                        <i class="fa fa-minus-circle mr-1"></i> 完成
                                    </button>
                                </div>
                            </div>
                        `;
                        
                        statsContainer.appendChild(card);
                    });
                })
                .catch(error => {
                    console.error('Error loading stats:', error);
                    showMessage('错误', '加载统计数据失败，请稍后重试', 'error');
                });
        }
        
        // 生成测试项
        function generateTask() {
            const limsNo = document.getElementById('lims_no').value.trim();
            const locationNo = document.getElementById('location_no').value.trim();
            const registerTime = document.getElementById('register_time').value;
            
            if (!limsNo) {
                showMessage('错误', 'LIMS号不能为空', 'error');
                return;
            }
            
            if (!locationNo) {
                showMessage('错误', '库位号不能为空', 'error');
                return;
            }
            
            if (!registerTime) {
                showMessage('错误', '请选择登记时间', 'error');
                return;
            }
            
            const testItem1 = document.getElementById('test_item1').value;
            const testItem2 = document.getElementById('test_item2').value;
            const testItem3 = document.getElementById('test_item3').value;
            const client = document.getElementById('client').value;
            const trustee = document.getElementById('trustee').value;
            
            // 固定值（来自原代码）
            const partNo = "11M881672A";
            const material = "PC+ABS";
            const partLocation = "6-2";
            const isTotal = "否";
            
            // 计算预计完成时间（17天后）
            const dueDate = new Date(registerTime);
            dueDate.setDate(dueDate.getDate() + 17);
            const dueDateStr = dueDate.toISOString().split('T')[0];
            
            // 实验项目
            const experimentItem = `${testItem1}, ${testItem2}, ${testItem3}`;
            
            const taskData = {
                lims_no: limsNo,
                location_no: locationNo,
                register_time: registerTime,
                test_item1: testItem1,
                test_item2: testItem2,
                test_item3: testItem3,
                client: client,
                trustee: trustee,
                part_no: partNo,
                is_total: isTotal,
                material: material,
                part_location: partLocation,
                due_time: dueDateStr,
                experiment_item: experimentItem
            };
            
            fetch('/api/tasks', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(taskData)
            })
            .then(response => response.json())
            .then(data => {
                if (data.success) {
                    showMessage('成功', '生成测试项成功！', 'success');
                    
                    // 清空表单
                    document.getElementById('lims_no').value = '';
                    document.getElementById('location_no').value = '';
                    
                    // 刷新数据
                    loadTasks();
                    loadStats();
                } else {
                    showMessage('错误', data.message || '生成测试项失败', 'error');
                }
            })
            .catch(error => {
                console.error('Error generating task:', error);
                showMessage('错误', '生成测试项失败，请稍后重试', 'error');
            });
        }
        
        // 更新完成任务数
        function updateCompleted(person, newCompleted) {
            if (newCompleted < 0) {
                showMessage('错误', '完成数不能小于0', 'error');
                return;
            }
            
            fetch('/api/stats', {
                method: 'PUT',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({
                    person: person,
                    completed: newCompleted
                })
            })
            .then(response => response.json())
            .then(data => {
                if (data.success) {
                    showMessage('成功', `已更新${person}的完成任务数`, 'success');
                    loadStats();
                } else {
                    showMessage('错误', data.message || '更新失败', 'error');
                }
            })
            .catch(error => {
                console.error('Error updating stats:', error);
                showMessage('错误', '更新失败，请稍后重试', 'error');
            });
        }
        
        // 显示消息模态框
        function showMessage(title, message, type) {
            const modal = document.getElementById('messageModal');
            const modalTitle = document.getElementById('modalTitle');
            const modalMessage = document.getElementById('modalMessage');
            const modalIcon = document.getElementById('modalIcon');
            
            modalTitle.textContent = title;
            modalMessage.textContent = message;
            
            // 设置图标和颜色
            if (type === 'success') {
                modalIcon.className = 'w-16 h-16 mx-auto mb-4 flex items-center justify-center rounded-full bg-green-100 text-green-500 text-2xl';
                modalIcon.innerHTML = '<i class="fa fa-check"></i>';
            } else if (type === 'error') {
                modalIcon.className = 'w-16 h-16 mx-auto mb-4 flex items-center justify-center rounded-full bg-red-100 text-red-500 text-2xl';
                modalIcon.innerHTML = '<i class="fa fa-times"></i>';
            } else if (type === 'warning') {
                modalIcon.className = 'w-16 h-16 mx-auto mb-4 flex items-center justify-center rounded-full bg-yellow-100 text-yellow-500 text-2xl';
                modalIcon.innerHTML = '<i class="fa fa-exclamation-triangle"></i>';
            } else {
                modalIcon.className = 'w-16 h-16 mx-auto mb-4 flex items-center justify-center rounded-full bg-blue-100 text-blue-500 text-2xl';
                modalIcon.innerHTML = '<i class="fa fa-info-circle"></i>';
            }
            
            // 显示模态框
            modal.classList.remove('hidden');
            modal.classList.add('flex');
            
            // 添加动画
            setTimeout(() => {
                const modalContent = modal.querySelector('div');
                modalContent.classList.add('scale-100');
                modalContent.classList.remove('scale-95');
            }, 10);
        }
        
        // 关闭模态框
        function closeModal() {
            const modal = document.getElementById('messageModal');
            const modalContent = modal.querySelector('div');
            
            modalContent.classList.remove('scale-100');
            modalContent.classList.add('scale-95');
            
            setTimeout(() => {
                modal.classList.add('hidden');
                modal.classList.remove('flex');
            }, 200);
        }
    </script>
</body>
</html>
    
