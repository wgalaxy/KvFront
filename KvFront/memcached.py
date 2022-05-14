 #   Copyright (C) 2017-2022  Gavin W
 #   This program is free software: you can redistribute it and/or modify
 #   it under the terms of the GNU General Public License as published by
 #   the Free Software Foundation, either version 3 of the License, or
 #   (at your option) any later version.

 #   This program is distributed in the hope that it will be useful,
 #   but WITHOUT ANY WARRANTY; without even the implied warranty of
 #   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 #   GNU General Public License for more details.

 #   You should have received a copy of the GNU General Public License
 #   along with this program.  If not, see <http://www.gnu.org/licenses/>.
 
import memcache

class MemcachedHelper:
    
    def set(self, key, value, time):
        setRet = self.mc.set(key, value, time)
        return setRet
    
    def get(self, key):
        setRet = self.mc.get(key)
        return setRet
    
    def stats(self):
        setRet = self.mc.get_stats()
        return setRet
    
    def connect(self, ip):
        self.mc = memcache.Client(ip, debug=False)
            
    def close(self):
        if self.mc is not None:
            self.mc.disconnect_all()   
        
    def get_multi(self, keys):
        vals = self.mc.get_multi(keys)
        return vals
    
    def delete_multi(self, keys):
        deleteRet = self.mc.delete_multi(keys)
        return deleteRet
    
    def flush(self):
        self.mc.flush_all()


    def __init__(self):
        self.mc = None
        
