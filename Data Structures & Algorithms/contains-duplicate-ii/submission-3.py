class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        window = set() # window de taille k maximum ?
        l = 0
        

        for r in range(len(nums)):
            if r - l> k:  # si window > k alors on enleve la valeur du left et on increment le left pointer ?
               window.remove(nums[l])
               l += 1
            if nums[r] in window: # si r dans window alors duplicate on return true, on ajoute r dans window, et si tjrs rien a la fin false
                return True
            window.add(nums[r])
        return False