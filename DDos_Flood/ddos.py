import requests
import threading

def flood(url, num_requests):
	for _ in range(num_requests):
		try:
			response = requests.get(url)
			print(f"Response Code: {response.status_code}")
		except requests.RequestException as e:
			print(f"Reuest Failed: {e}")

def main():
	url = "http://127.0.0.1:8050"
	num_threads = 10
	requests_per_thread = 50

	threads = []
	for _ in range(num_threads):
		thread = threading.Thread(target=flood, args=(url, requests_per_thread))
		threads.append(thread)
		thread.start()
	
	for thread in threads:
		thread.join()

if __name__=="__main__":
	main()
