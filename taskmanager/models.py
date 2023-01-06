from taskmanager import db


class Category(db.Model):
    # scheam for the category model
    id = db.Column(db.Integer, primary_key=True)
    category_name = db.Column(db.String(25), unique=True, nullable=True)
    tasks = db.relationship(
        "Task", backref="category", cascade="all, delete", lazy=True
    )

    def __repr_(self):
        return self.category_name


class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    task_name = db.Column(db.String(50), unique=True, nullable=False)
    task_description = db.Column(db.Text, nullable=False)
    is_urgent = db.Column(db.Boolean, default=False, nullable=False)
    due_date = db.Column(db.Date, nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey(
        'category.id', ondelete='CASCADE'
    ), nullable=True)

    def __repr_(self):
        return "#{0} - Task: {1} | Urgent: {2}".format(
            self.id, self.task_name, self.is_urgent
        )
