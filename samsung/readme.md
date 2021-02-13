# Endpoints Avaliable

- `/relationship`
- `/about`

  [watch the working video](https://youtu.be/W35eh0jdGP4)

# steps to follow for docker

- To build the docker

> Be in the project folder
> `sudo docker build --tag interview_task .`

> `sudo docker run --network=host --name interview_task -p 5001:5001 interview_task`

## setps after docker up

> To see the ouptut url: `http://127.0.0.1:5001/relationship`
> with body

```{"relation":[{"parent": "node_1", "child": "node_4"},
        {"parent": "node_2", "child": "node_4"},
        {"parent": "node_3", "child": "node_4"},
        {"parent": "node_4", "child": "node_5"},
        {"parent": "node_4", "child": "node_7"},
        {"parent": "node_6", "child": "node_5"}],
"node_ids":["node_5", "node_7", "node_4"]}
```

- output:

```
  "node_4": [
  "node_1",
  "node_2",
  "node_3",
  "node_4"
  ],
  "node_5": [
  "node_1",
  "node_2",
  "node_3",
  "node_4",
  "node_5",
  "node_6"
  ],
  "node_7": [
  "node_1",
  "node_2",
  "node_3",
  "node_4",
  "node_7"
  ]

}
```
