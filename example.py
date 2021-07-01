import asyncio
from scrapli import Scrapli
from scrapli.driver.core import AsyncIOSXEDriver
from device_list import DEVICES
import ipdb
from rich import print as rprint
async def gather_version(device):

  conn = AsyncIOSXEDriver(**device)
  await conn.open()
  presult= await conn.get_prompt()
  vresult= await conn.send_command("show version")
  sresult= vresult.genie_parse_output()["version"]["version_short"]
  sresult2= vresult.textfsm_parse_output()
  #ipdb.set_trace()
  for x in sresult2:
         w=x['hostname']
         y=x['serial']
         z=x['uptime']

  await conn.close()
  #print(w,y,z)
  return w,y,z

async def main():
   coroutiness = [gather_version(device) for device in DEVICES]
   result = await asyncio.gather(*coroutiness)
   #ipdb.set_trace()
   for resu in result:
         rprint(f"[green]Device: {resu[0]}[/green]" , 'and' ,f"[red]SN: {resu[1]}[/red]",' and',f"[yellow]uptime: {resu[2]}[/yellow]")
         #rprint(f"[white]---------------------------")
         #rprint(f"[red]SN: {resu[1]}[/red]")
         #rprint(f"[white]---------------------------")
         #rprint(f"[yellow]uptime: {resu[2]}[/yellow]")
         #rprint(f"[blue]---------------------------")
        #print(resu[x])
   #ipdb.set_trace()
asyncio.run(main())
'''
ver1=ver[nnn][0].scrapli_response.textfsm_parse_output()
#pprint(ver1)
for int in ver1:
    w=int['version']
    s=int['serial']
    u=int['uptime']
    h=int['hostname']

def show_version():
  ver = nr.run(task=send_command, command="show version")
  for nnn in nn:
     ver1=ver[nnn][0].scrapli_response.textfsm_parse_output()
     #pprint(ver1)
     for int in ver1:
         w=int['version']
         s=int['serial']
         u=int['uptime']
         h=int['hostname']
         #print('The serial for switch ',nnn,' is',Fore.RED+s[0],' and hostname' , Fore.GREEN+h)
         SwiIp.append([nnn,s[0]])
'''
