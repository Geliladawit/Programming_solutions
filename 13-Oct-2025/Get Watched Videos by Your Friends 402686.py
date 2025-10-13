# Problem: Get Watched Videos by Your Friends - https://leetcode.com/problems/get-watched-videos-by-your-friends/description/

class Solution:
    def watchedVideosByFriends(self, watchedVideos: List[List[str]], friends: List[List[int]], id: int, level: int) -> List[str]:
        n = len(friends)
        visited = set([id])
        queue = deque([id])
        current_level = 0

        while queue and current_level < level:
            for _ in range(len(queue)):
                person = queue.popleft()
                for f in friends[person]:
                    if f not in visited:
                        visited.add(f)
                        queue.append(f)
            current_level += 1
            level_friends = list(queue)

        video_count = Counter()
        for f in level_friends:
            video_count.update(watchedVideos[f])

        sorted_videos = sorted(video_count.keys(), key=lambda x: (video_count[x], x))

        return sorted_videos