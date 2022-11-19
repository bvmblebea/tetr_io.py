from requests import get

class TetrIO:
	def __init__(self) -> None:
		self.api = " https://ch.tetr.io/api"
		self.headers = {
			"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36"
		}

	def get_server_statistics(self) -> dict:
		return get(
			f"{self.api}/general/stats",
			headers=self.headers).json()

	def get_server_activity(self) -> dict:
		return get(
			f"{self.api}/general/activity",
			headers=self.headers).json()

	def get_user_info(self, username: str) -> dict:
		return get(
			f"{self.api}/users/{username}",
			headers=self.headers).json()

	def get_user_records(self, username: str) -> dict:
		return get(
			f"{self.api}/users/{username}/records",
			headers=self.headers).json()

	def get_league_leaderboard(
			self,
			after: int = 25000,
			before: int = None,
			limit: int = 50,
			country: str = "US") -> dict:
		url = f"{self.api}/users/lists/league?limit={limit}&country={country}"
		if after:
			url += f"&after={after}"
		if before:
			url += f"&before={before}"
		return get(url, headers=self.headers).json()

	def get_league_leaderboard_full(
			self,
			country: str = "US") -> dict:
		return get(
			f"{self.api}/users/lists/league/all?country={country}",
			headers=self.headers).json()

	def get_xp_leaderboard(
			self,
			after: int = 25000,
			before: int = None,
			limit: int = 50,
			country: str = "US") -> dict:
		url = f"{self.api}/users/lists/xp?limit={limit}&country={country}"
		if after:
			url += f"&after={after}"
		if before:
			url += f"&before={before}"
		return get(url, headers=self.headers).json()

	def get_stream_info(self, stream: str) -> dict:
		return get(
			f"{self.api}/steams/{stream}",
			headers=self.headers).json()

	def get_latest_news(self, limit: int = 25) -> dict:
		return get(
			f"{self.api}/news?limit={limit}",
			headers=self.headers).json()

	def get_stream_latest_news(self, stream: str, limit: int = 25) -> dict:
		return get(
			f"{self.api}/news/{stream}?limit={limit}",
			headers=self.headers).json()
