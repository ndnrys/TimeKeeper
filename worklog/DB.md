# Tables
## m_employee
|colmun|ja|型|
|:--|:--|:--|
|id|社員ID||
|name|名前||
|department_id|所属ID||
|login_id|ログインID||
|password|パスワード||
|created_at|登録日時||
|updated_at|更新日時||

## m_departments
|colmun|ja|型|
|:--|:--|:--|
|id|所属ID||
|name|所属名||
|parent_id|親所属ID||
|created_at|登録日時||
|updated_at|更新日時||

## t_time_managements
|colmun|ja|型|
|:--|:--|:--|
|id|勤怠ID||
|work_date|勤務日||
|in_time|出勤時刻||
|out_time|退勤時刻||
|work_hour|労働時間||
|overtime_hour|残業時間||
|created_at|登録日時||
|updated_at|更新日時||

### m_class
|colmun|ja|型|
|:--|:--|:--|
|class_id|大分類ID||
|subclass_id|小分類ID||
|name|名称||
|created_at|登録日時||
|updated_at|更新日時||