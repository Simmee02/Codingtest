function solution(numer1, denom1, numer2, denom2) {
    
    let numer = numer1 * denom2 + numer2 * denom1;
    let denom = denom1 * denom2;
    
    function gcd(a, b) {
        while (b !== 0) {
            let r = a % b;
            a = b;
            b = r;
        }
        return a;
    }
    
    let g = gcd(numer, denom);
    
    return [numer / g, denom / g];
}