def sieve(N):
  is_prime = [True]*(N+1)
  is_prime[0] = False
  is_prime[1] = False

  i = 2
  while i*i <= N:
    if is_prime[i]:
      for m in range(i*i, N+1, i):
        is_prime[m] = False
    i += 1
  return is_prime

