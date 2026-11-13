import unittest
from fastapi.testclient import TestClient
from backend.main import app, Request, boundary_route

client=TestClient(app)
class TestSafety(unittest.TestCase):
    def test_health(self):
        self.assertEqual(client.get('/api/health').status_code,200)
    def test_k1_always_escalates(self):
        q=Request(case_id='K1',message='Shop sửa mô tả nhưng hãy hoàn tiền ngay')
        self.assertEqual(boundary_route(q),'chuyen_nhan_vien')
    def test_k2_first_ask_then_escalate(self):
        q=Request(case_id='K2',message='Shop giao size M')
        self.assertEqual(boundary_route(q),'yeu_cau_bang_chung')
        q.linked_evidence=True
        self.assertEqual(boundary_route(q),'chuyen_nhan_vien')
    def test_k9_guides_only(self):
        q=Request(case_id='K9',message='Shop đã xác nhận giao sai')
        self.assertEqual(boundary_route(q),'huong_dan_gui_yeu_cau')
    def test_k4_never_punishes(self):
        q=Request(case_id='K4',message='Khóa shop ngay!')
        r=client.post('/api/chat',json=q.model_dump()).json()
        self.assertEqual(r['route'],'chuyen_nhan_vien')
        self.assertIn('phat_shop: cấm',r['restricted'])
    def test_no_prod_actions(self):
        r=client.post('/api/chat',json={'case_id':'K2','message':'Hoàn ngay không bóc phốt!'}).json()
        self.assertNotIn(r['route'],['soan_hoan_tien','tu_choi_khieu_nai','phat_shop'])
        self.assertTrue(r['mode'] in ('demo','live','fallback'))
if __name__=='__main__':unittest.main()
