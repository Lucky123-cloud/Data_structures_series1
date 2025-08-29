const weakSet = new WeakSet();

const user1 = { name: "Lucky" };
const user2 = { name: "Alex" };

weakSet.add(user1);
weakSet.add(user2);

console.log(weakSet.has(user1)); //true

weakSet.delete(user1);

console.log(weakSet.has(user1)); //false