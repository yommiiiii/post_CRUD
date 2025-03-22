from flask import Flask, render_template, request, redirect
import pymysql

app = Flask(__name__)

# MySQL DB 연결
db = pymysql.connect(
    host='localhost',
    user='root',
    password='yumin1095',
    database='board_db',
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor
)

# 메인 페이지 - 게시글 목록 & 검색 기능
@app.route('/')
def index():
    keyword = request.args.get('keyword', '')
    category = request.args.get('category', '')

    cursor = db.cursor()

    if keyword and category:
        like_keyword = f"%{keyword}%"
        if category == 'title':
            sql = "SELECT * FROM posts WHERE title LIKE %s ORDER BY created_at DESC"
            cursor.execute(sql, (like_keyword,))
        elif category == 'content':
            sql = "SELECT * FROM posts WHERE content LIKE %s ORDER BY created_at DESC"
            cursor.execute(sql, (like_keyword,))
        else:  # 제목 + 내용
            sql = "SELECT * FROM posts WHERE title LIKE %s OR content LIKE %s ORDER BY created_at DESC"
            cursor.execute(sql, (like_keyword, like_keyword))
    else:
        sql = "SELECT * FROM posts ORDER BY created_at DESC"
        cursor.execute(sql)

    posts = cursor.fetchall()
    return render_template('index.html', posts=posts, keyword=keyword, category=category)

# 글 작성 페이지 (GET) - 글 작성 폼 보여줌
@app.route('/create', methods=['GET'])
def create_form():
    return render_template('create.html')

# 글 작성 처리 (POST) - DB에 새 글 저장
@app.route('/create', methods=['POST'])
def create_post():
    title = request.form['title']
    content = request.form['content']
    cursor = db.cursor()
    sql = "INSERT INTO posts (title, content) VALUES (%s, %s)"
    cursor.execute(sql, (title, content))
    db.commit()
    return redirect('/')

# 글 상세 보기
@app.route('/post/<int:post_id>')
def view_post(post_id):
    cursor = db.cursor()
    sql = "SELECT * FROM posts WHERE id = %s"
    cursor.execute(sql, (post_id,))
    post = cursor.fetchone()
    return render_template('view.html', post=post)

# 글 수정 페이지 (GET) - 기존 글 내용 보여줌
@app.route('/update/<int:post_id>', methods=['GET'])
def update_form(post_id):
    cursor = db.cursor()
    cursor.execute("SELECT * FROM posts WHERE id = %s", (post_id,))
    post = cursor.fetchone()
    return render_template('update.html', post=post)

# 글 수정 처리 (POST) - DB에서 수정 반영
@app.route('/update/<int:post_id>', methods=['POST'])
def update_post(post_id):
    title = request.form['title']
    content = request.form['content']

    cursor = db.cursor()
    sql = "UPDATE posts SET title = %s, content = %s WHERE id = %s"
    cursor.execute(sql, (title, content, post_id))
    db.commit()

    return redirect(f'/post/{post_id}')

# 글 삭제
@app.route('/delete/<int:post_id>')
def delete_post(post_id):
    cursor = db.cursor()
    sql = "DELETE FROM posts WHERE id = %s"
    cursor.execute(sql, (post_id,))
    db.commit()
    return redirect('/')

# 애플리케이션 실행
if __name__ == '__main__':
    app.run(debug=True)
