from minio import Minio
from minio.error import S3Error


def main():
    # Create a client with the MinIO server playground, its access key
    # and secret key.
    client = Minio(
        "localhost:9000", access_key="altair", secret_key="12345678", secure=False   
    )

    all_buckets = client.list_buckets()

    for bucket in all_buckets:

        print(f"bucket name: {bucket.name}")

        try:

            count = 0

            all_objects = client.list_objects(bucket.name, recursive=True)

            for obj in all_objects:
                
                count += 1

                print(count ,obj.object_name)

        except S3Error as err:

            print(err)

    client.fget_object(
        bucket_name="asiatrip", object_name="asiaphotos-2015.txt", file_path="test.txt"
    )

if __name__ == "__main__":
    try:
        main()
    except S3Error as exc:
        print("error occurred.", exc)