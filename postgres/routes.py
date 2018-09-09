

from views import AddUser,UserDetails,RmoveUser 
class GetRoutes():
    @staticmethod
    def fetch_routes(app):
        
        app.add_url_rule('/api/levelup/adduser',
                         view_func=AddUser.as_view('add'), methods=['POST',])
        
        app.add_url_rule('/api/levelup/users',
                         view_func=UserDetails.as_view('all'),
                         defaults={'user_id': None}, methods=['GET',])
        app.add_url_rule('/api/levelup/users/<int:user_id>',
                         view_func=UserDetails.as_view('one'), methods=['Get',])
        
        
        app.add_url_rule('/api/levelup/users/<user_id>',
                         view_func=RmoveUser.as_view('removed'), methods=['DELETE',])
        