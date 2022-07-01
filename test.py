from com.util.getConfig import Config

con = Config()
if con.get_config_bool('scheduler', 'is_scheduler'):
    print(1111)

days = con.get_config_int('scheduler', 'days')
params = ''
if days is not None:
    params = params + ', ' + 'weeks=' + str(days)
print(params)

