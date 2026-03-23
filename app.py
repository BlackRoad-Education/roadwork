#!/usr/bin/env python3
"""RoadWork — AI Tutoring Platform"""
import json, sys, sqlite3, os, random
from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import urlparse, parse_qs

DB = os.path.expanduser("~/.blackroad/roadwork.db")
SUBJECTS = [
    {"id": "math", "name": "Mathematics", "mastery": 72, "topics": ["Algebra", "Calculus", "Statistics", "Number Theory"]},
    {"id": "physics", "name": "Physics", "mastery": 45, "topics": ["Mechanics", "Thermodynamics", "Electromagnetism", "Quantum"]},
    {"id": "cs", "name": "Computer Science", "mastery": 83, "topics": ["Algorithms", "Data Structures", "Networks", "OS"]},
    {"id": "music", "name": "Music Theory", "mastery": 38, "topics": ["Harmony", "Rhythm", "Composition", "Ear Training"]},
    {"id": "writing", "name": "Writing", "mastery": 61, "topics": ["Structure", "Voice", "Revision", "Research"]},
    {"id": "quantum", "name": "Quantum Computing", "mastery": 22, "topics": ["Qubits", "Gates", "Entanglement", "Algorithms"]},
]
QUIZZES = {
    "math": [{"q": "What is the derivative of x^3?", "options": ["3x^2", "x^2", "3x", "x^3"], "answer": 0},
             {"q": "What is the integral of 2x?", "options": ["x^2 + C", "2x^2", "x", "2"], "answer": 0}],
    "cs": [{"q": "What is the time complexity of binary search?", "options": ["O(log n)", "O(n)", "O(n^2)", "O(1)"], "answer": 0},
           {"q": "Which data structure uses LIFO?", "options": ["Stack", "Queue", "Tree", "Graph"], "answer": 0}],
}

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        p = urlparse(self.path)
        if p.path == "/api/subjects": self.respond(200, SUBJECTS)
        elif p.path.startswith("/api/quiz/"):
            subj = p.path.split("/")[-1]
            self.respond(200, {"subject": subj, "questions": QUIZZES.get(subj, [{"q": "Coming soon", "options": ["A","B","C","D"], "answer": 0}])})
        elif p.path == "/api/chat":
            q = parse_qs(p.query).get("q", [""])[0]
            self.respond(200, {"response": f"Great question about '{q}'. Let me explain: this concept connects to the fundamental principles we covered earlier. The key insight is that understanding comes from practice, not memorization.", "agent": "lucidia"})
        elif p.path == "/": self.serve_html()
        else: self.respond(404, {"error": "Not found"})
    def respond(self, code, data):
        self.send_response(code); self.send_header("Content-Type", "application/json"); self.send_header("Access-Control-Allow-Origin", "*"); self.end_headers()
        self.wfile.write(json.dumps(data).encode())
    def serve_html(self):
        self.send_response(200); self.send_header("Content-Type", "text/html"); self.end_headers()
        self.wfile.write(b"<html><body style='background:#0a0a0a;color:#f5f5f5;font-family:sans-serif;padding:40px;max-width:600px;margin:0 auto'><h1>RoadWork</h1><p style='color:#737373'>AI tutoring that adapts to you.</p><div id='s'></div><script>fetch('/api/subjects').then(r=>r.json()).then(d=>{document.getElementById('s').innerHTML=d.map(s=>'<div style=\"background:#131313;border:1px solid #1a1a1a;border-radius:10px;padding:16px;margin:8px 0\"><b>'+s.name+'</b> <span style=\"color:#525252\">'+s.mastery+'%</span><div style=\"height:4px;background:#1a1a1a;border-radius:2px;margin-top:8px\"><div style=\"height:100%;width:'+s.mastery+'%;background:#404040;border-radius:2px\"></div></div></div>').join('')})</script></body></html>")
    def log_message(self, *args): pass

if __name__ == "__main__":
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 5001
    print(f"RoadWork running on :{port}")
    HTTPServer(("0.0.0.0", port), Handler).serve_forever()
