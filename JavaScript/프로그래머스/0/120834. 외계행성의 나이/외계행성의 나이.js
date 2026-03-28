function solution(age) {
    let arr = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j'];
    return String(age).split('').map(v => arr[v]).join('');
}