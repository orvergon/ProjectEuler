import qualified Data.Map as Map

divisors :: Int -> [Int]
divisors n = [x | x <- [1..n `div` 2], n `mod` x == 0]

primes' :: [Int] -> [Int]
primes' [] = []
primes' (x:xs) = [x] ++ (primes' . filter (\n -> n `mod` x /= 0)) xs

primes = primes' [2..]

factor :: [Int] -> Int -> [Int]
factor _ 1 = []
factor [] _ = []
factor ps n = if n `mod` ph == 0 then [ph] ++ factor ps (n `div` ph)
  else factor pts n
  where
    ph = head ps
    pts = tail ps

multiply :: [Int] -> [Int]
multiply [] = [1]
multiply (x:xs) = [foldr (*) 1 (x:xs)] ++ multiply xs

group :: [Int] -> [[Int]]
group [] = []
group (x:xs) = [multiply slice] ++ group rest
  where
    slice = filter (x ==) (x:xs)
    rest = drop (length slice) (x:xs)

divisors' :: Int -> [Int]
divisors' = ds 
  where
    ds = tail . map (foldr (*) 1) . sequence . group . factor primes

--99s
--16s - 14s
