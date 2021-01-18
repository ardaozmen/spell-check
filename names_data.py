import pandas as pd

df = pd.read_csv('calisan_data.csv')
namelist=df['Isimler'].to_list()
surnamelist=df['Soyisimler'].to_list()

def listToString(s):
	str1 = ' '

	for ele in s:
		str1 += ele + ','
	return str1


names=listToString(namelist)
surnames=listToString(surnamelist)
total=(names+surnames)

def main():
	f=open("words.txt", "w+")
	f.write(total)
	f.close()
if __name__=="__main__":
	main()
