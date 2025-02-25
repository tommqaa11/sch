from flask import Flask, render_template, jsonify
from datetime import datetime
import json

app = Flask(__name__)

# 课程数据
schedules = {
    'user1': {
        'morning': [
            {
                'time': '08:00 - 08:45',
                'courses': [
                    {
                        'name': '博弈论',
                        'location': '卓越楼333',
                        'day': 1,
                        'span': 2
                    },
                    {
                        'name': '云计算技术',
                        'location': '一教332',
                        'day': 2,
                        'span': 2
                    },
                    {
                        'name': '多元统计与分析',
                        'location': '卓越楼527',
                        'day': 4,
                        'span': 2
                    }
                ]
            },
            # ... 其他课程数据 ...
        ]
    }
    # ... 其他用户数据 ...
}

def handler(event, context):
    """
    Netlify Function handler
    """
    path = event.get('path', '/')
    
    if path == '/':
        return {
            'statusCode': 200,
            'headers': {
                'Content-Type': 'text/html',
            },
            'body': render_template('schedule.html')
        }
    
    elif path.startswith('/get_schedule/'):
        user = path.split('/')[-1]
        if user not in schedules:
            return {
                'statusCode': 404,
                'body': json.dumps({'error': 'User not found'})
            }
        
        return {
            'statusCode': 200,
            'headers': {
                'Content-Type': 'text/html',
            },
            'body': render_template('schedule_content.html', schedule=schedules[user])
        }
    
    return {
        'statusCode': 404,
        'body': json.dumps({'error': 'Not found'})
    } 