import qualified Data.Map as Map

divisors :: Int -> [Int]
divisors n = [x | x <- [1..n `div` 2], n `mod` x == 0]

amicables :: Int -> Int -> [Int]
amicables s e = [x | (x, y) <- ns, y <= e && x /= y && (sum . divisors) y == x]
  where
   ns = [(x, (sum . divisors) x) | x <- [s..e]]

--using map
amicables' :: Int -> Int -> [(Int, Int)]
amicables' s e = Map.foldrWithKey (\ k x ms -> if k /= x && Map.member x ns && ns Map.! x == k then [(k, x)] ++ ms else [] ++ ms) [] ns
  where
   ns = Map.fromList[(x, (sum . divisors) x) | x <- [s..e]]

--using oly list
amicables'' :: Int -> Int -> [Int]
amicables'' s e = as
  where
   ns = [(x, (sum . divisors) x) | x <- [s..e]]
   as = [x | (x, y) <- ns, x /= y && (sum . divisors) y == x]
