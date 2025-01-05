import pymysql
try:
    connection = pymysql.connect(
        host='localhost',
        user='root',
        password='root',
        db='new_house',
        charset='utf8',
        cursorclass=pymysql.cursors.DictCursor
    )
    print(connection)
except Exception as e:
    print(e)


# <!DOCTYPE html>
# <html lang="zh">
#
# <head>
#     <meta charset="UTF-8">
#     <meta name="viewport" content="width=device-width, initial-scale=1.0">
#     <title>房屋搜索和租赁</title>
#     <style>
#         body {
#             font-family: Arial, sans-serif;
#             background-color: #f4f4f4;
#             margin: 0;
#             padding: 0;
#             display: flex;
#             flex-direction: column;
#             align-items: center;
#         }
#
#         h1, h2 {
#             color: #333;
#             text-align: center;
#             margin: 20px 0;
#         }
#
#         a {
#             color: #007bff;
#             text-decoration: none;
#             margin-bottom: 20px;
#         }
#
#         a:hover {
#             text-decoration: underline;
#         }
#
#         .search-bar {
#             display: flex;
#             flex-wrap: wrap;
#             justify-content: space-between;
#             align-items: flex-start; /* Align items at the top of each column */
#             gap: 10px;
#             padding: 20px;
#             background: #fff;
#             border-radius: 8px;
#             box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
#             margin-bottom: 20px;
#         }
#
#         /* Update the input styles within the search-bar */
#         .search-bar input[type="number"],
#         .search-bar input[type="text"],
#         .search-bar select {
#             flex: 1; /* Make input fields take equal width */
#             padding: 10px;
#             margin: 0;
#             border: 1px solid #ddd;
#             border-radius: 4px;
#             /* Adjust the width to your preference */
#             min-width: 150px;
#         }
#
#         .search-bar button {
#             background-color: #007bff;
#             color: white;
#             border: none;
#             padding: 10px 15px;
#             border-radius: 4px;
#             cursor: pointer;
#             transition: background-color 0.3s ease;
#         }
#
#         .search-bar button:hover {
#             background-color: #0056b3;
#         }
#
#         .houses-container {
#             display: flex;
#             flex-wrap: wrap;
#             justify-content: space-around;
#             gap: 20px;
#         }
#
#         .house {
#             flex: 1;
#             background: #fff;
#             border: 1px solid #ddd;
#             border-radius: 4px;
#             padding: 20px;
#             box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
#         }
#
#         @media (max-width: 800px) {
#             .house {
#                 flex: 0 0 calc(50% - 20px);
#             }
#         }
#
#         @media (max-width: 500px) {
#             .search-bar {
#                 flex-direction: column;
#             }
#
#             .house {
#                 flex: 0 0 100%;
#             }
#         }
#     </style>
# </head>
#
# <body>
#     <h1>搜索房屋</h1>
#     <a href="/tenant_home/">返回主页</a>
#
#     <form method="GET" class="search-bar">
#         最小面积：<input type="number" name="min_area" min="0">
#         最大面积：<input type="number" name="max_area" min="0">
#         位置：<input type="text" name="location">
#         布局：<input type="text" name="layout">
#         最小租金：<input type="number" name="min_rent" min="0">
#         最大租金：<input type="number" name="max_rent" min="0">
#         <label for="status">状态:</label>
#         <select id="status" name="status">
#             <option value="all">所有状态</option>
#             <option value="available">可出租</option>
#             <option value="unavailable">不可出租</option>
#         </select>
#         <button type="submit" name="search">搜索</button>
#     </form>
#
#     <h2>房屋列表</h2>
#     <div class="houses-container">
#         <form method="POST">
#             {% csrf_token %}
#             {% for house in houses %}
#             <div class="house">
#                 <h3>房屋编号：{{ house.house_number }}</h3>
#                 <p>面积：{{ house.area }} 平方米</p>
#                 <p>位置：{{ house.location }}</p>
#                 <p>布局：{{ house.layout }}</p>
#                 <p>月租金：{{ house.monthly_rent }} 元</p>
#                 <p>状态：{{ house.status }}</p>
#                 <p>可租用日期：{{ house.available_from }}</p>
#                 <p>租赁条款：{{ house.lease_terms }}</p>
#
#                 {% if house.status != '不可出租' %}
#                 <input type="radio" id="house_{{ house.id }}" name="house_id" value="{{ house.id }}">
#                 <label for="house_{{ house.id }}">选择这个房子</label>
#                 {% else %}
#                 <p>不可出租</p>
#                 {% endif %}
#             </div>
#             {% endfor %}
#
#             <label for="rent_duration">租房时间（月份）:</label>
#             <input type="number" id="rent_duration" name="rent_duration" min="1" placeholder="月份">
#
#             <button type="submit" name="rent_house">租房</button>
#         </form>
#
#         {% if selected_house %}
#         <h2>租房信息</h2>
#         <p>选中的房屋：{{ selected_house.title }}</p>
#         <p>房租：{{ cost }}</p>
#         <p>手续费：{{ fee }}</p>
#         <p>总费用：{{ total_cost }}</p>
#         <p>租赁时间：{{ selected_rent_duration }} 个月</p>
#         {% endif %}
#     </div>
# </body>
#
# </html>